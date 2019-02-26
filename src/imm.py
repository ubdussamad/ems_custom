# EMS Core Utils
# Ref: 12Feb2019
# Author: ubdussamad <ubdussamad@gmail.com>
# IMM ( Inventory Management Module)
import sqlite3
import time
import math

DEBUG = False
VERBOSE_DEBUG = False

class imm ( object ):
    def __init__ ( self , id):
        self.id = id
        self.server = sqlite3.connect('%s.db'%self.id)
        self.cursor = self.server.cursor()
    def create_db (self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ivn(P_id TEXT,Quantity REAL,Unit TEXT,Unit_Rate REAL,Description TEXT)")

    def update( self, p_id, u_type, data ):
        # Here i am strictly assuming that the p_id wouldn't be negative.
        if u_type == 'chk_out':
            # Decreasing the Quatity of stock of the specific product_id
            self.cursor.execute('UPDATE ivn SET Quantity = Quantity - (?) WHERE P_id = (?)', (data[0] ,p_id))
            self.server.commit()

        elif u_type == 'append_stk':
            # Decreasing the Quatity of stock of the specific product_id
            self.cursor.execute('UPDATE ivn SET Quantity = Quantity + (?) WHERE P_id = (?)', (data[0] ,p_id))
            self.server.commit()
        elif u_type == 'del_product':
            # Deleting the product completely from the inventory
            self.cursor.execute('DELETE FROM ivn WHERE P_id = (?)', (p_id,))
            self.server.commit()
            
        elif u_type == 'total_update':
            # Updating Data of an Specific Product
            data = (*data,p_id)
            query = "UPDATE ivn SET Quantity = \'%s\',Unit = \'%s\',Unit_Rate = \'%s\',Description = \'%s\',Tax = \'%s\' WHERE P_id = \'%s\';"%(data)
            self.cursor.execute(query)
            self.server.commit()
        else:
            print("Bad Update Type!")
            return(-1)

    def append_ivn ( self , data ):
        #Checks and adds Content to the inventory
        self.cursor.execute("INSERT INTO ivn ( P_id, Quantity, Unit, Unit_Rate, Description , Tax ) VALUES (?,?,?,?,?,?)",
                            (*data,))
        self.server.commit()
    def return_item_names(self):
        self.cursor.execute('SELECT P_id FROM ivn')
        data = self.cursor.fetchall()
        return(data)

    def scarce( self ):
        self.cursor.execute('SELECT P_id, Quantity , Unit FROM ivn ORDER BY Quantity ASC')
        data = self.cursor.fetchall()
        return(data)


    
    def delete(self, p_id):
        self.cursor.execute('DELETE FROM ivn WHERE P_id = (?)',(p_id,))
        self.server.commit()
        
    def search ( self , product= ''):
        # Returns a subsetset of self.data contaning the keywords
        # Returns a list of lists containing only names whic matcvh it
        if not product:self.cursor.execute('SELECT * FROM ivn')
        else:self.cursor.execute('SELECT * FROM ivn WHERE P_id LIKE (?)',
                                    (product+"%",))
        data = self.cursor.fetchall()
        return(data)

if __name__ == "__main__":
    some  = imm('ems')
