from posture import *
from event import *

class myWere(protagonist):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(myWere, cls).__new__(cls, *args, **kwargs)
		return cls._instance
	def __init__(self,name = "Garou"):
		self.name = name
		#Multiplier for skill mastery
		self.aptitude = 5
		self.flags = {}
		self.initMoods()
		self.initSkills()
	def initMoods(self):
		#Initializing moods
		self.mood.addMood(nervous,excited,0)			#Relaxed, Aggresive
		self.mood.addMood(sad,happy,0)					#passive, Dominant
		self.mood.addMood(passive,dominant,2)			#nervous, excited
		self.mood.addMood(relaxed,aggressive,1)			#sad, happy
		#The hardest two moods to get into should be:		
	def initPerformance(self):
		#Initializing Skills
		#Good Bad
		G = [dominant,nervous]
		B = [relaxed,sad]
		self.skills.addSkill(posturing,performance,G,B)
		G = [passive,sad]
		B = [dominant,nervous]
		self.skills.addSkill(dignity,performance,G,B)
		G = [relaxed]
		B = [nervous,excited]
		self.skills.addSkill(grace,performance,G,B)
	def initAthletics(self):
		#Initializing Skills
		#Good Bad
		G = [aggressive]
		B = [relaxed]
		self.skills.addSkill(strength,athletics,G,B)
		G = [relaxed]
		B = [aggressive]
		self.skills.addSkill(constitution,athletics,G,B)
		G = [happy,excited]
		B = [sad]
		self.skills.addSkill(speed,athletics,G,B)		
	def initObediance(self):
		#Initializing Skills
		#Good Bad
		G = [passive]
		B = [dominant,aggressive]
		self.skills.addSkill(submission,obedience,G,B)
		G = [relaxed]
		B = [nervous,excited]
		self.skills.addSkill(patience,obedience,G,B)
		G = [happy]
		B = [sad]
		self.skills.addSkill(memory,obedience,G,B)
	def initSkills(self):
		self.initAthletics()
		self.initPerformance()
		self.initObediance()
	def description(self):
		pos = poses(str(self.mood))
		ret = ""
		ret += "At full height, your werewolf "+self.name+" is seven feet tall. "+pos.d1()+", two triangular ears "+pos.d2()+" A Shaggy brown main covers broad shoulders, running down his back into a long unkempt tail. Another, much shorter layer of grey fur covers the brute's muscular chest, thick arms and powerful digitigrade legs. The wolf's front paws, though shaped like human hands, boast ten dull claws, cracked and chipped by poor care. Like a wolf's, his jaws boast many white sharp teeth. "+pos.d3() 
		ret += "\n"
		ret += "\n"
		ret +=  pos.d4()+" "+pos.d5()+" "+pos.d6()+" a cheap rope, from the corner of the room. He wears a plain collar."
		ret += "\n"
		ret += "\n"
		ret += "He seems fairly "+str(self.mood)
		return ret


