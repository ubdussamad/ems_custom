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
import time,sqlite3,base64
import os.path

def main ( *args , **kwargs ) :
    # Will be using some C-style Control for ease in debugging
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
            self.total_amount += tmp + tmp*float(i[4]) if not ttype else tmp #Custom Rate + Tax
            self.imm.update( i[0] , 'chk_out' , [i[1]])


        if payment_type == "current" and not ttype:  #Logging the transaction in the cmm
            self.cmm.update( self.c_id , 'u_acc' ,self.total_amount)
        elif payment_type == "borrow" and not ttype: # 2 ask
            # Borrowing
            self.cmm.update( self.c_id , 'd_add' ,self.total_amount)
        if ttype:
            #log somewhere else
            pass

        transaction_id = int(time.time())
        date = str(time.ctime())
        if not ttype:  # Logging the transaction in the log
            self.lmm.append_log([transaction_id,date,self.c_id,
                             self.total_amount,','.join([i[0] for i in self.cart])])
        else:
            self.__log_untaxed([ transaction_id, self.c_id, date , self.total_amount , ','.join([i[0] for i in self.cart]) ])

        self.recipt = self.genrate_recipt(transaction_id,date,payment_type,
                            self.total_amount , ttype)

    def genrate_recipt(self,t_id,date, p_type,total_amount,ttype=0):
        data = []
        for i in self.cart:
            amount = float(i[1])*float(i[3])
            tax = (float(i[4])/100)*amount if not ttype else 0
            total = amount+(tax if not ttype else 0)
            data.append(i+[tax,total])
        recipt = { "Transaction Id":t_id , "Date":date ,
                   "data":data , "Billed by": self.agent,
                   "Payment Type": p_type , "Total Amount":total_amount , "Client": self.c_id}
        return(recipt)
    def display_ivn(self, p_id = ''):
        return self.imm.search(p_id)
    def id2c(self,id):
        return(self.cmm.id_to_client(id)[0])
    def c2id(self,cl):
        return(self.cmm.client_to_id(cl))
if __name__ == "__main__":
    some = ems_core('ems','admin')
    some.add_to_cart('RED_NORMAL',20,12)
    some.display_cart()
    some.add_to_cart('BLUE_NORMAL',5,20)
