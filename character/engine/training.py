#this will group associated skills
class catagory:
	def __init__(self,name):
		#Total mastery within a catagory
		self.totalm = 0
		self.name = name
	def __str__(self):
		return self.name

#this will measue proficiancy in skills
class skill:
	def __init__(self,name,catagory):
		self.moods = {}
		self.name = name
		self.mastery = 0
		self.catagory = catagory
	def __str__(self):
		ret = (self.name + " " + str(self.mastery))
		return ret
	def __getitem__(self,index):
		ret = 1
		index = str(index)
		if index in self.moods:
			ret = self.moods[index]
		return ret

class skills:
	def __init__(self):
		self.skills = {}
		#move to main later
	#To make another skill
	def addSkill(self,name,catagory,gmoods = [],bmoods = []):
		self.skills[name] = skill(name,catagory)
		for gmood in gmoods:
			self.skills[name].moods[gmood] = 2
		for bmood in bmoods:
			self.skills[name].moods[bmood] = .5
	def __str__(self):
		ret = ""
		for skill in self.skills:
			ret += " ("+str(self.skills[skill])+") "
		return ret
	def __getitem__(self,index):
		return self.skills[index]
