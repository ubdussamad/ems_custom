# EMS Core Utils
# Ref: 12Feb2019
# Author: ubdussamad <ubdussamad@gmail.com>
# CMM ( Client Management Module)
import sqlite3
import time
import datetime
import math,os

DEBUG  = 0
VERBOSE_DEBUG = 0

class cmm ( object ):
        def __init__( self , id):
                self.id = id
                self.server = sqlite3.connect(os.path.join('data','%s.db'%self.id))
                self.cursor = self.server.cursor()

        def create_db (self):
                self.cursor.execute("CREATE TABLE IF NOT EXISTS cmm(C_id REAL,Client TEXT,Due REAL,Unit TEXT,Net_Transactions REAL ,Description TEXT)")

        def delete(self, c_id):
                self.cursor.execute('DELETE FROM cmm WHERE C_id = (?)',(c_id,))
                self.server.commit()
        def is_user( self , c_id ):
                self.cursor.execute('SELECT * FROM cmm where C_id = (?)',(c_id,))
                l = self.cursor.fetchone()
                return( bool(l) )

        def update (self , c_id , action=False , amount=0 , data = [] ):
                # Clear dues , Change names et-cetra.
                # NOte: Once Registered, You can't change the client id.
                self.create_db()
                if DEBUG:print("C_id:",c_id)
                self.cursor.execute('SELECT * FROM cmm where C_id = (?)',(c_id,))
                l = self.cursor.fetchone()

                if not l:
                        print("Invaild Client Key!")
                        return(-1)

                if action: #Due Adding/Clearing Routine
                        if action=='d_clr':
                                self.cursor.execute('UPDATE cmm SET Due = Due - (?) WHERE C_id = (?)', (amount ,c_id))
                        elif action=='d_add':
                                self.cursor.execute('UPDATE cmm SET Due = Due + (?), Net_Transactions = Net_Transactions + (?)  WHERE C_id = (?)', (amount, amount ,c_id))
                        elif action == 'u_acc':
                                self.cursor.execute('UPDATE cmm SET Net_Transactions = Net_Transactions + (?) WHERE C_id = (?)',
                                                    (amount ,c_id))
                        else:
                                print("Bad Checkout!")
                                return(-1)
                        self.server.commit()
                else:   #Client TEXT,Due REAL,Unit TEXT,Net_Transactions REAL ,Description TEXT)
                        data = ( *list(map(str,data)), str(c_id))
                        #print(data)
                        query = "UPDATE cmm SET Client = \'%s\',Due = %s,Unit = \'%s\',Net_Transactions = %s ,Description = \'%s\' WHERE C_id = %s;"%data
                        self.cursor.execute(query)
                        self.server.commit()

        def append ( self , data ):
                #Checks and adds Content to the inventory
                c_id = int(time.time()) # Fresh Unique Customer id Generation
                self.cursor.execute("INSERT INTO cmm(C_id,Client,Due,Unit,Net_Transactions,Description) VALUES (?,?,?,?,?,?)",
                                    ( c_id, *data ))
                self.server.commit()
        def client_details(self,client):
                return(self.search(client)[0])
        def client_to_id ( self , client ):
                data = self.search(client)
                return ( data[0][0] )
        def id_to_client (self , id):
            self.cursor.execute('SELECT (Client) FROM cmm where C_id = (?)',(id,))
            data = self.cursor.fetchall()
            return(data[0])
        def c2id (self ,client):
            self.cursor.execute('SELECT (C_id) FROM cmm where Client LIKE (?)',(str(client)+'%',))
            data = self.cursor.fetchall()
            return(data)
        def list_c_names( self ):
                self.cursor.execute('SELECT (Client) FROM cmm')
                data = self.cursor.fetchall()
                return(data)
        def dues( self ):
                self.cursor.execute('SELECT Client, Due, Unit FROM cmm ORDER BY Due DESC')
                data = self.cursor.fetchall()
                return(data)

        def search ( self, client =''):
                if not client:self.cursor.execute('SELECT * FROM cmm ORDER BY Due DESC')
                else:self.cursor.execute('SELECT * FROM cmm WHERE Client LIKE (?) ORDER BY Due DESC',
                                    (client+"%",))
                data = self.cursor.fetchall()
                return(data)


if __name__ == "__main__":
        some  = cmm("../ems")
