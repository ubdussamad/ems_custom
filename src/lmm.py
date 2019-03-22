# EMS Core Utils
# Ref: 12Feb2019
# Author: ubdussamad <ubdussamad@gmail.com>
# LMM ( Log / Hisotry Management Module)
import sqlite3
import time
import datetime
import math

DEBUG  = 0
VERBOSE_DEBUG = 0

class lmm ( object ):
        def __init__( self , id):
                self.id = id
                self.server = sqlite3.connect('%s.db'%self.id)
                self.cursor = self.server.cursor()
                
        def create_db (self):
                self.cursor.execute("CREATE TABLE IF NOT EXISTS hmm( T_id REAL, Time TEXT, C_id REAL, Net_Amt REAL, Products TEXT)")

        def update ( self, t_id ):
                #Deleting routines
                self.cursor.execute('DELETE FROM hmm WHERE T_id = (?)', (t_id,))
                self.server.commit()
                
        def append_log ( self, data ):
                self.cursor.execute("INSERT INTO hmm (T_id, Time, C_id, Net_Amt, Products) VALUES (?,?,?,?,?)",(*data,))
                self.server.commit()

        def most_bought(self):
                self.cursor.execute('SELECT Products FROM hmm') 
                data = self.cursor.fetchall()
                products = []
                for i in data:
                        l = [k.split('|')[0] for k in i[0].split(',')]
                        for j in l:
                                products.append(j)
                s = set(products)
                dic = {}
                for i in s:
                        k = len([ j for j in products if j == i])
                        dic[i] = k
                data = []
                for i in dic:
                        data.append([i,dic[i]])
                data = sorted(data,key=lambda x: (x[1],x[0]))[::-1]
                return(data)
                
        def search ( self , key = '' ,  key_type = 0):
                # Returns a subsetset of self.data contaning the keywords
                # Return a list of lists containing only fileds which have closure
                # Key types are -> 0:Transaction ID // 1: Date and time // 2: Customer  
                if not key:
                        self.cursor.execute('SELECT * FROM hmm')
                elif key_type == 0:
                        self.cursor.execute('SELECT * FROM hmm WHERE T_id LIKE (?)',
                                    (key+"%",))
                elif key_type == 1:
                        self.cursor.execute('SELECT * FROM hmm WHERE Time LIKE (?)',
                                    (key+"%",))
                elif key_type == 2:
                        # Must write a routine to convert Customer name to C_id
                        self.cursor.execute('SELECT * FROM cmm WHERE Client LIKE (?)',
                                    (key+"%",))
                        try:
                                tmp = self.cursor.fetchall()[0][0]
                        except:
                                return []
                        self.cursor.execute('SELECT * FROM hmm WHERE C_id = (?)',
                                    (tmp,))
                else:
                        self.cursor.execute('SELECT * FROM hmm')
                data = self.cursor.fetchall()
                return(data)


if __name__ == "__main__":
        some = lmm('ems')
