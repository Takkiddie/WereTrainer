from were import *

class moodEvent(baseEvent):
	def exeStory(self):
		return str(self.pro.mood)
class playFetch(moodEvent):
	def exeStory(self):
		ret = ""
		self.pro.mood.changeMood(happy)
		self.pro.mood.changeMood(relaxed)
		ret += "You play fetch with "
		ret += self.pro.name+". "
		ret += "The physical activity calms him, "
		ret += "but he enjoys himself."
		return ret;
class massage(moodEvent):
	def exeStory(self):
		ret = ""
		self.pro.mood.changeMood(happy)
		self.pro.mood.changeMood(passive)
		self.pro.mood.changeMood(relaxed)
		ret += "You take "
		ret += self.pro.name
		ret += " To get a massage. "
		ret += "It relaxes him a lot."
		return ret;
class bath(moodEvent):
	def exeStory(self):
		ret = ""
		self.pro.mood.changeMood(passive)
		self.pro.mood.changeMood(passive)
		self.pro.mood.changeMood(aggressive)
		self.pro.mood.changeMood(sad)
		ret += "You give "
		ret += self.pro.name
		ret += "a bath. "
		ret += "He doesn't like getting sprayed down, "
		ret += "but he holds firm under your orders."
		return ret;
class park(moodEvent):
	def exeStory(self):
		ret = ""
		self.pro.mood.changeMood(dominant)
		self.pro.mood.changeMood(dominant)
		self.pro.mood.changeMood(relaxed)
		ret += "You take "
		ret += self.pro.name
		ret += "to the park. "
		ret += "All the showing off wears him out a bit."
		return ret;
class watchPerformance(moodEvent):
	def exeStory(self):
		#if more passive than dominant
		ret = ""
		self.pro.mood.changeMood(nervous)
		self.pro.mood.changeMood(passive)
		ret += "You show "
		ret += self.pro.name
		ret += "some of your past trainees' performances. "
		ret += "Seeing the standards he'll have to live up to "
		ret += "puts him on edge, but he seems more willing to listen."		
		return ret;
class news(moodEvent):
	def exeStory(self):
		ret = ""
		self.pro.mood.changeMood(nervous)
		self.pro.mood.changeMood(sad)
		ret += "You have "
		ret += self.pro.name
		ret += " Watch a news show. "
		ret += "Seeing how big and intimidating the world is "
		ret += "puts him on edge."		
		return ret;
#Equivalent to prison
class opponents(moodEvent):
	def exeStory(self):
		ret = "You show Garou a few videos of the potential competition.\n"
		if self.pro.mood[nervous] >= 0:
			ret += "Seeing such talented foes makes him nervous.\n"
			self.pro.mood.changeMood(nervous)
			self.pro.mood.changeMood(sad)
		else:
			ret += "Undaunted, Garou seems excited to fight the new meat.\n"
			self.pro.mood.changeMood(excited)
			self.pro.mood.changeMood(aggressive)			
		return ret;
	
#Re do all of these
#Static
	#tour gardens		+happy			+relaxed				XplayFetch
	#play with toys,	+happy			+relaxed	+passive	Xmassage
	#Attend Court, 		+2passive		+aggressive	+sad		Xbath
	#sneak out, 		+2dominant		+relaxed				Xpark
	#Explore Castle		+nervous		+passive (relaxed)		XwatchPerformance
	#Visit Grave		+nervous		+sad					Xnews
#Dynamic
	#Dungeon, Dominant/Excited	or...	Nervous/Relaxed			(Finish this)
	#Attend Service									
#Unlockable static
	#Tresury			+aggressive	(+excited)
	#sports				+excited	-passive
#Unlockable Dynamic
	#dancing			+dominant	+happy	or +sad if dominant
	#hunting			-Angry/Afraid