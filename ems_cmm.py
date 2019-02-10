# EMS Utils
# Contains:
# IMM ( Inventory Management Module)
# LMM ( Log / Hisotry Management Module)
# CMM ( Client Management Module)
import datetime
debug = 1
verbose = 0
class cmm ( object ):
	def __init__ ( self , id):
		self.i_id = id # Inventory Id 
		self.i_name = None # Inventory Name
		self.data = None #This is a list of lists
	
	#Routine for loading and parsing data into class object
        #defined by the inventory id
	def parse_log ( self ):
                try:
                        with open('cmm.log','r') as f_obj:
                                log = f_obj.read().strip('\n')
                                f_obj.close()
                                log = log.split('\n')
                                log = [i.split('%sep') for i in log]
                                self.data = log
                                if debug and verbose:print("Parsed File")
                except:
                        print("File Error, Bad file.!")
                        exit()
                        
        def test_print (  self, *args ):
                for i in self.data:
                        print(i)

	def update ( self , key , data , dec_qty = False , qty=0): # Clear dues et-cetra
                #Data is a list contaning all fields of a specific item
                #The problem is to form data
                self.parse_log()
                print (key)
                index = None
                for i in self.data:
                        if i[0] == key:
                                index = self.data.index(i)
                if index == None:
                        print("Invaild key!")
                        return(-1)
                elif dec_qty: #Special Quantity Decremnt Routine for faster processing
                        if float(self.data[index][1]) < qty:
                                print("STOCK PROBLEM")
                                return(-2)
                        self.data[index][1] = str(float(self.data[index][1])-qty)
                else:
                        self.data[index] = data
                self.relog()
        def relog ( self ):
                print("Re Logging")
                try:
		        with open('cmm.log','w') as f_obj:
                                for i in self.data:
                                        line = str('%sep'.join(i)+'\n')
                                        f_obj.write(line)
                                f_obj.flush()
                                f_obj.close()
                                if debug and verbose:print("Update File File")
                except Excecption as err:
                        print("File Error, Bad file.! : %s"%err)
                        exit()
        def append ( self , c_name , due ,unit , t_trans ,desc , new=0 ):
                #Checks and adds Content to the inventory
                try:
                        z,k=float(due),float(t_trans)
                        del z
                        del k
                except:
                        print("Wrong entry, Use numbers for amount and rate")
                        return(-2)
                #Parse them nicely
                try:
                        with open('cmm.log','w' if new else 'a') as f_obj:
                                line = str('%sep'.join([c_name,due,unit,t_trans,desc])+'\n')
                                f_obj.write(line)
                                f_obj.flush()
                                f_obj.close()
                                if debug and verbose:print("Added new items to inventory.")
                except:
                        print("No log to append")
	def search ( self , key):
		# Returns a subsetset of self.data contaning the keywords
                # Return a list of lists containing only names whic matcvh it
                self.parse_log()
		if key == '':
                        return self.data
                elif key:
                        tmp = filter(None,[i if key.lower() in i[0].lower() else None for i in self.data])
                        return(tmp)
                else:
                        return self.data
        
	def check_out( self , data ):
		# Will Communicate with LMM and possibly CMM
		# TODO:
		# 1. Parse Cart data
		# 2. Modify inventory data as per cart data
		# 3. Generate Recipt
		return

	def balance_check_out ( self , data ,customer_id ):
		# Modify data as per future leads
		return

some  = cmm( 112 )
some.parse_log()
some.test_print()
d  =['BLUE_NORMAL', '50', 'Kg', '15', 'Just a blue color']
