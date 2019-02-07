# EMS Utils
# Contains:
# IMM ( Inventory Management Module)
# LMM ( Log / Hisotry Management Module)
# CMM ( Client Management Module)


class imm ( object ):
	def __init__ ( self , id):
		self.i_id = id # Inventory Id 
		self.i_name = None # Inventory Name
		self.data = None
	
	#Routine for loading data into class object defined by the inventory id
	def load ( self ):
		try:
			self.data = load_i(self.i_id)
			return(0)
		except:
			return("0x1")

	def update ( self ):
		self.load(self)

	def search ( self  , key):
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
