# EMS Utils
# Contains:
# IMM ( Inventory Management Module)
# LMM ( Log / Hisotry Management Module)
# CMM ( Client Management Module)
import datetime
debug = 1
verbose = 0
class imm ( object ):
	def __init__ ( self , id):
		self.i_id = id # Inventory Id 
		self.i_name = None # Inventory Name
		self.data = None #This is a list of lists
	
	#Routine for loading and parsing data into class object
        #defined by the inventory id
	def parse_log ( self ):
                try:
		        with open('ivn.log','r') as f_obj:
                                log = f_obj.read()
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

	def update ( self , key , field ):
                self.parse_log()

                if field == 0:
                        if debug:print("Editing PID")
                        return
                elif field == 1:
                        if debug:print("Editing Amount")
                        return
                elif field == 2:
                        if debug:print("Editing Unit")
                        return
                elif field == 3:
                        if debug:print("Editing Rate")
                        return
                elif field == 4:
                        if debug:print("Editing Description")
                        return
                else:
                        print("Invalid key")
                        return(-1)

	def search ( self , key):
		# Will be done after planing data format
		return

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

some  = imm ( 112 )
some.parse_log()
some.test_print()
some.update("RED_NORMAL" , 1 )
some.update("RED_NORMAL" , 2 )
some.update("RED_NORMAL" , 3 )
some.update("RED_NORMAL" , 4 )
some.update("RED_NORMAL" , 5 )
some.update("RED_NORMAL" , 0 )
