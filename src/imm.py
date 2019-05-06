# EMS Core Utils
# Ref: 12Feb2019
# Author: ubdussamad <ubdussamad@gmail.com>
# IMM ( Inventory Management Module)
import sqlite3
import time
import math,os

DEBUG = False
VERBOSE_DEBUG = False

class imm ( object ):
    def __init__ ( self , id):
        self.id = id
        self.server = sqlite3.connect(os.path.join('data','%s.db'%self.id))
        self.cursor = self.server.cursor()
    def create_db (self):
        pass
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS ivn(P_id TEXT,Quantity REAL,Unit TEXT,Unit_Rate REAL,Description TEXT)")

    def update( self, p_id, u_type, data ):
        # Here i am strictly assuming that the p_id wouldn't be negative.
        if u_type == 'chk_out':
            # Decreasing the Quatity of stock of the specific product_id
            self.cursor.execute('SELECT Quantity FROM ivn WHERE P_id LIKE (?)',(p_id,))
            qty = self.cursor.fetchall()[0][0]
            if qty < float(data[0]):
                data[0] = qty
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
            query = "UPDATE ivn SET Quantity = \'%s\',Unit = \'%s\',Unit_Rate = \'%s\',Description = \'%s\',Tax = \'%s\', `HSN/SAC` = \'%s\' , Stock_Price = \'%s\'   WHERE P_id = \'%s\';"%(data)
            self.cursor.execute(query)
            self.server.commit()

        elif u_type == 'mod_rate':
            data = (*data,p_id)
            query = "UPDATE ivn SET stkp_history = \'%s\' WHERE P_id = \'%s\';"%(data)
            self.cursor.execute(query)
            self.server.commit()
        else:
            print("Bad Update Type!")
            return(-1)
    def get_mod_rate( self, p_id):
        self.cursor.execute('SELECT stkp_history FROM ivn WHERE P_id = (?)',(p_id,))
        data = self.cursor.fetchone()[0] #25:30,27:60
        data = data.split(',') if data else []
        return(data)



    def append_ivn ( self , data ):
        #Checks and adds Content to the inventory
        self.cursor.execute("INSERT INTO ivn ( `P_id`, `Quantity`, `Unit`, `Unit_Rate`, `Description`, `Tax` ,`HSN/SAC`, `Stock_Price`) VALUES (?,?,?,?,?,?,?,?)",
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

    def search ( self , product= '',key = 'P'):
        # Returns a subsetset of self.data contaning the keywords
        # Returns a list of lists containing only names whic matcvh it
        if not product:self.cursor.execute('SELECT * FROM ivn')
        else:
            if key=='P':
                self.cursor.execute('SELECT * FROM ivn WHERE P_id LIKE (?)',
                                    (product+"%",))
            elif key=='H':
                self.cursor.execute('SELECT * FROM ivn WHERE \"HSN/SAC\" LIKE (?)',
                                    (product+"%",))
            else:
                self.cursor.execute('SELECT * FROM ivn')

        data = self.cursor.fetchall()
        return(data)

if __name__ == "__main__":
    some  = imm('../ems')
