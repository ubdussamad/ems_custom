# EMS Utils
# Contains:
# IMM ( Inventory Management Module)
# LMM ( Log / Hisotry Management Module)
# CMM ( Client Management Module)
import datetime

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
                                self.log = f_obj.read()
                                self.log = self.log.split('\n')
                                self.log = [i.split('||') for i in self.log]
		except:
			return("0x1")

	def update ( self ):
		self.load(self)

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
