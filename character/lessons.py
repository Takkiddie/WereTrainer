from were import *

#Interface
#Never to be implemented
class lessonEvent(baseEvent):
	def __init__(self,protag):
		self.pro = protag
		self.subInit()
	def subInit(self):
		raise NotImplementedError("implement subInit");
	def displayData(self):
		return str(self.pro.skills)
	def exeStory(self):
		self.pro.applyLesson(self.lesson)
		return self.learned
class teachStrength(lessonEvent):
	def subInit(self):
		self.lesson = strength
		self.learned = "You have "+self.pro.name+" lift weights. "
		self.learned += "He's strong, already quite strong, so you teach him proper technique."	
class teachConstitution(lessonEvent):
	def subInit(self):
		self.lesson = constitution
		self.learned = "You have "+self.pro.name+" jog to build his stamina."	
class teachSpeed(lessonEvent):
	def subInit(self):
		self.lesson = speed
		self.learned = "You play games with "+self.pro.name+" to hone his reflexes."	
class teachSubmission(lessonEvent):
	def subInit(self):
		self.lesson = submission
		self.learned = "You have "+self.pro.name+" lay down, roll over, and do other very basic, tricks. "	
		self.learned += "There's some arguing before he swallows his pride and listens."
		self.learned += "You finally get him to, grudgingly, lay down."
class teachPatience(lessonEvent):
	def subInit(self):
		self.lesson = patience
		self.learned = "You have "+self.pro.name+" perform menial frustrating tasks. "	
		self.learned += "Each time he loses his temper he has to start over."
class teachMemory(lessonEvent):
	def subInit(self):
		self.lesson = memory
		self.learned = "You have "+self.pro.name+" play memory games. "	
		self.learned += "This will help him follow complex instructions."
class teachPosturing(lessonEvent):
	def subInit(self):
		self.lesson = posturing
		self.learned = "You have "+self.pro.name+" practice looking scary at a mirror. "	
		self.learned += "You teach him exactly what gestures to use to appear just threatening enough."
class teachDignity(lessonEvent):
	def subInit(self):
		self.lesson = dignity
		self.learned = "You have "+self.pro.name+" practice looking refined. "	
		self.learned += "Mostly it's about posture and voice."
class teachGrace(lessonEvent):
	def subInit(self):
		self.lesson = grace
		self.learned = "You have "+self.pro.name+" practice moving with grace. "	
		self.learned += "Balance and posture are key."

#Skills:
#strength
#constitution
#speed
#submission
#patience
#memory
#posturing
#dignity
#grace


