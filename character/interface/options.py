from were import *
from display import *

#Make Singleton
class optionMenu:
	def options(self,options):
		disp.options = options
		disp.dispWhat = "options"

		while disp.chosen == "":
			pass
		disp.dispWhat = "talk"
		ret = disp.chosen
		disp.chosen = ""
		disp.options = ["default","dofault"]
		return ret
		