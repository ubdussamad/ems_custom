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
import time
import sqlite3

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
        self.cart = [] # [[p_id , qty]]
        self.c_id = 0
        self.recipt = {}
    def display_cart(self):
        return(self.cart)
    def add_to_cart(self, p_id, qty, rate ):
        self.cart.append( [p_id , qty , rate] )
    def change_cid ( self, client ):
        self.c_id = self.cmm.client_to_id( client )
    def clear_session(self):
        self.cart = []
        self.c_id = 0
    def check_out ( self , payment_type):
        # Deduct the inventory *
        # --> Process Amount *
        # Modify the client details *
        # Log the transaction (Once per order)*
        # Genrate the Recipt *
        if self.cart == []:
            print("Empty Cart")
            return(-1)
        self.total_amount = 0
        for i in self.cart:
            self.total_amount += float(i[1])*float(i[2]) #Custom Rate
            self.imm.update( i[0] , 'chk_out' , [i[1]])
        

        if payment_type == "current":
            self.cmm.update( self.c_id , 'u_acc' ,self.total_amount)
        elif payment_type == "borrow":
            # Borrowing
            self.cmm.update( self.c_id , 'd_add' ,self.total_amount)
        transaction_id = int(time.time())
        date = str(time.ctime())
        self.lmm.append_log([transaction_id,date,self.c_id,
                             self.total_amount,','.join([i[0] for i in self.cart])])
        self.recipt = self.genrate_recipt(transaction_id,date,payment_type,
                            self.total_amount)

                            
    def genrate_recipt(self,t_id,date, p_type,total_amount):
        data = [ i+[i[1]*i[2]] for i in self.cart]
        recipt = { "Transaction Id":t_id , "Date":date ,
                   "data":data , "Billed by": self.agent,
                   "Payment Type": p_type , "Total Amount":total_amount , "Client": self.c_id}
        return(recipt)
if __name__ == "__main__":
    some = ems_core('ems','kallu')
    some.add_to_cart('RED_NORMAL',20,12)
    some.display_cart()
    some.add_to_cart('BLUE_NORMAL',5,20)
