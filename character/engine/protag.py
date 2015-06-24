from moods import *
from training import *

#Your player character's class
class protagonist:
	mood = wereMoods()
	skills = skills()
	name = ""
	aptitude = 0
	def __init__(self,name = "Garou"):
		self.name = name
		self.initMoods()
		self.initSkills()
	def moodMod(self,skill):
		return self.skills[skill][self.mood]
	def getMods(self):
		ret = ""
		for skill in self.skills.skills:
			skill = self.skills[skill]
			#If the skill is not affected by the mood
			mod = skill[str(self.mood)]
			if mod != 1:
				ret += " ("
				ret += skill.name
				ret += " "
				ret += str(mod)
				ret += ")"
		return ret
	def applyLesson(self,skill):
		learned = self.moodMod(skill)*self.aptitude
		self.skills[skill].mastery += learned


