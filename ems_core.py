# Bismillah-he ar-Rehman ar-Rahim
# EMS - Custom
# Ref: 6Feb2018
# Version: 0.1
# Author: Mohammed S. Haque <ubdussamad@gmail.com>
# Contract For: Mr Nouman
# Copyright 2019 EMD Systems.

from src import cmm
from src import lmm
from src import imm
import time,sqlite3,base64,time
import os.path

def main ( *args , **kwargs ) :
    # Will be using self C-style Control for ease in debugging
    return(0)

class ems_core ( object):
    def __init__(self,dbid,agent):
        self.dbid = dbid
        self.agent = agent
        self.cmm = cmm.cmm(self.dbid)
        self.lmm = lmm.lmm(self.dbid)
        self.imm = imm.imm(self.dbid)
        self.cmm.create_db()
        self.lmm.create_db()
        self.imm.create_db()

        # List of all the items for the session
        self.cart = [] # [[p_id , qty , unit,rate , tax]]
        self.c_id = 0
        self.recipt = {}



    def __encode(self,key, clear):
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def __decode(self,key, enc):
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)

    def __log_untaxed(self,data):
        path = 'resources/config_integrity.config'
        self.__key = 'emscustom'
        # Data is of format: time_stamp as t_id , c_id , time , amount , products
        with open(path, 'a' if os.path.isfile(path) else 'w' ) as file_pointer:
            data = '&sep'.join(map(str,data))
            data = self.__encode(self.__key , data)
            file_pointer.write(data+'\n')
            file_pointer.flush()
            file_pointer.close()

    def display_cart(self):
        return(self.cart)

    def add_to_cart(self, p_id, qty, unit, rate , tax ):
        self.cart.append( [p_id , qty  , unit, rate , tax] )

    def change_cid ( self, client ):
        self.c_id = self.cmm.client_to_id( client )

    def clear_session(self):
        self.cart = []
        self.c_id = 0

    def display_all_customers(self):
        return self.cmm.list_c_names()

    def calc_profit(self,data,ttype = 0):
        print("Profit routine called!")
        def floatify(x):
            try:return(float(x))
            except:return(x)

        cp,sp,tax = 0,0,0
        for i in data: #Data is cart and i is items in the Cart
            p_id = i[0]  #modrate looks like: 25:30,27:60
            # i loks like [p_id , qty  , unit, rate , tax]
            i = list(map(floatify,i))
            modrate = self.imm.get_mod_rate(p_id)
            #print("\nPid is: %s \n Modrate: %s and Qty: %s"%(p_id,modrate,str(i[1]))
            modrate = { float(i.split(':')[0]):float(i.split(':')[1]) for i in modrate if i}
            sp += i[1]*i[3] # Selling price
            # Here i[1] is the qty in cart
            tax += (i[4]/100)*i[1]*i[3] # tax amount
            last_mod_rate = 0
            for j in modrate:
                if modrate[j] >= i[1]: # PArtial Stock > demand
                    cp += j * i[1] # Cost price
                    modrate[j] -= i[1]
                    break
                else:
                    last_mod_rate = j
                    cp += modrate[j] * j
                    i[1] -= modrate[j]
                    modrate[j] = 0
            if i[1] > 0.0:
                print("Forced Sale extra amount: %.2f\nCp till now: %.2f"%(i[1],cp))
                cp += last_mod_rate*i[1]

            modrate = ["%.3f:%.3f"%(i,modrate[i]) for i in modrate if modrate[i]]
            modrate = ','.join(modrate)
            self.imm.update(p_id,'mod_rate',[modrate])

        profit_for_sale = sp - cp
        print("Profit: %.3f"%profit_for_sale)
        print("Tax: %.3f \n Cp: %.3f \n Sp: %.3f"%(tax,cp,sp))
        if not ttype:
            # Normal transaction
            t = time.ctime()
            date,month,year = t[8:10],t[4:7],t[-4:]
            self.lmm.cursor.execute( "SELECT * FROM stats WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\' "%(date,month,year) )
            is_existant = self.lmm.cursor.fetchall()

            if is_existant:
                self.lmm.cursor.execute("UPDATE stats SET `Profit Salewise` = `Profit Salewise` + \'%s\' , Tax = Tax + \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(profit_for_sale,str(tax),date,month,year))
            else:
                self.lmm.cursor.execute("INSERT INTO stats (`Year`,`Month`,`Date`,`Expense`,`Profit Salewise`,`Tax`,`key`) VALUES (?,?,?,?,?,?,?)",
                                        (year,month,date,'0.0',str(profit_for_sale),str(tax),'0.0'))
            self.lmm.server.commit()
        else:
            t = time.ctime()
            date,month,year = t[8:10],t[4:7],t[-4:]
            self.lmm.cursor.execute( "SELECT * FROM stats WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\' "%(date,month,year) )
            is_existant = self.lmm.cursor.fetchall()

            if is_existant:
                self.lmm.cursor.execute("UPDATE stats SET `key` = `key` + \'%s\' WHERE Date=\'%s\' AND Month=\'%s\' AND Year=\'%s\'"%(profit_for_sale,date,month,year))
            else:
                self.lmm.cursor.execute("INSERT INTO stats (`Year`,`Month`,`Date`,`Expense`,`Profit Salewise`,`Tax`,`key`) VALUES (?,?,?,?,?,?,?)",
                                        (year,month,date,'0.0','0.0','0.0',str(profit_for_sale)))
            self.lmm.server.commit()
        return('%.3f,%.3f'%(profit_for_sale,tax))


    def check_out ( self , payment_type , ttype = 0): #ttype = pk (0) / ka (1)
        # Deduct the inventory *
        # --> Process Amount *
        # Modify the client details *
        # Log the transaction (Once per order)*
        # Genrate the Recipt *
        if self.cart == []:
            print("Empty Cart") #Could go in status label
            return(-1)
        self.total_amount = 0
        for i in self.cart:
            tmp = float(i[1])*float(i[3])
            self.total_amount += tmp + tmp*(float(i[4])/100) if not ttype else tmp #Custom Rate + Tax
            self.imm.update( i[0] , 'chk_out' , [i[1]])
        print(self.total_amount)


        if payment_type == "current" and not ttype:  #Logging the transaction in the cmm
            self.cmm.update( self.c_id , 'u_acc' ,self.total_amount)
        elif payment_type == "borrow" and not ttype: # 2 ask
            # Borrowing
            self.cmm.update( self.c_id , 'd_add' ,self.total_amount)

        transaction_id = int(time.time())
        date = str(time.ctime())
        if not ttype:  # Logging the transaction in the log
            pt = self.calc_profit(self.cart,ttype)
            self.lmm.append_log([transaction_id,date,self.c_id,#P_id,qty,rate,tax , Billed BY
                             self.total_amount,','.join([i[0]+'|%.3f|%.3f|%.3f|'%tuple(map(float,(i[1],i[3],i[4]))) for i in self.cart]),self.agent,pt])

        else:
            pt = self.calc_profit(self.cart,ttype)
            self.__log_untaxed([ transaction_id, self.c_id, date , self.total_amount , ','.join([i[0]+'|%.3f|%.3f|%.3f|'%tuple(map(float,(i[1],i[3],i[4]))) for i in self.cart]),pt])

        self.recipt = self.genrate_recipt(transaction_id,date,payment_type,
                            self.total_amount , ttype)

    def genrate_recipt(self,t_id,date, p_type,total_amount,ttype=0):
        data = []
        for i in self.cart:
            amount = float(i[1])*float(i[3])
            tax = (float(i[4])/100)*amount if not ttype else 0
            total = amount+(tax if not ttype else 0)
            self.imm.cursor.execute('select `HSN/SAC` from ivn where P_id = (?)',(i[0],))
            hsn = self.imm.cursor.fetchone()
            # [[p_id , qty , unit,rate , tax]]
            #['GREEN_DARK', 'ABCDEF', '210.35 Kg', '50.0', '5' , '55000.0' ]
            data.append([str(i[0]),hsn[0], str(i[1])+i[2] , str(i[3]) , str(tax) , str(total)])
        recipt = { "Transaction Id":t_id , "Date":date ,
                   "data":data , "Billed by": self.agent,
                   "Payment Type": p_type , "Total Amount":total_amount , "Client": self.c_id}
        return(recipt)
    def display_ivn(self, p_id = '',key = 'P'):
        return self.imm.search(p_id,key)
    def id2c(self,id):
        return(self.cmm.id_to_client(id)[0])
    def c2id(self,cl):
        return(self.cmm.client_to_id(cl))
if __name__ == "__main__":
    self = ems_core('ems','admin')
    self.add_to_cart('RED_NORMAL',20,12)
    self.display_cart()
    self.add_to_cart('BLUE_NORMAL',5,20)
