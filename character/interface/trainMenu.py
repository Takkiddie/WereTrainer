from were import *
from display import *

#Make Singleton
class trainMenu:
	def train(self,options):
		self.options = list(options)
		#activity = input("Pick an activity: ")
		#Do a mood altering activity
		activity = self.menu()
		return activity
	def menu(self):
		disp.options = self.options
		disp.dispWhat = "options"

		while disp.chosen == "":
			pass
		disp.dispWhat = "talk"
		ret = disp.chosen
		disp.chosen = ""
		disp.options = ["default","dofault"]
		return ret
