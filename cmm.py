# EMS Core Utils
# Ref: 12Feb2019
# Author: ubdussamad <ubdussamad@gmail.com>
# CMM ( Client Management Module)
import sqlite3
import time
import datetime
import math

DEBUG  = 0
VERBOSE_DEBUG = 0

class cmm ( object ):
        def __init__( self , id):
                self.id = id
                self.server = sqlite3.connect('%s.db'%self.id)
                self.cursor = self.server.cursor()

        def create_db (self):
                self.cursor.execute("CREATE TABLE IF NOT EXISTS cmm(C_id REAL,Client TEXT,Due REAL,Unit TEXT,Net_Transactions REAL ,Description TEXT)")

        def update ( self , c_id , due_clr=False , deposit = 0.0 , data = [] ):
                # Clear dues , Change names et-cetra.
                # NOte: Once Registered, You can't change the client id.
                self.create_db()
                if DEBUG:print("C_id: %s"%c_id)
                self.cursor.execute('SELECT * FROM cmm where C_id = (?)',(c_id,))
                data = self.cursor.fetchone()

                if not data:
                        print("Invaild Client Key!")
                        return(-1)

                if due_clr: #Due Clearing Routine
                        self.cursor.execute('UPDATE cmm SET Due = Due - (?) WHERE C_id = (?)', (deposit ,c_id))
                        self.server.commit()
                else:
                        self.cursor.execute('UPDATE cmm SET(Client,Due,Unit,Net_Transactions,Description) = (?,?,?,?,?) WHERE C_id = (?)',
                                            (*data,c_id))
                        self.server.commit()
                
        def append ( self , data ):
                #Checks and adds Content to the inventory
                
                c_id = int(time.time()) # Fresh Unique Customer id Generation
                self.cursor.execute("INSERT INTO cmm(C_id,Client,Due,Unit,Net_Transactions,Description) VALUES (?,?,?,?,?,?)",
                                    ( c_id, *data ))
                self.server.commit()

        def search ( self, client =''):
                if not client:self.cursor.execute('SELECT * FROM cmm')
                else:self.cursor.execute('SELECT * FROM cmm WHERE Client LIKE (?)',
                                    (client+"%",))
                data = self.cursor.fetchall()
                return(data)


some  = cmm("ems")
