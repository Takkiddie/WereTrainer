from protag import *

class interfaceError(Exception):
	def __init__(self, value):
		self.value = value;
	def __str__(self):
		return str(self.value)
class baseEvent:
	def __init__(self,protag):
		self.pro = protag;
class desplayEvent(baseEvent):
	def displayData(self):
		ret = ""
		ret += self.pro.name + "\n"
		ret += str(self.pro.mood) + "\n"
		ret += str(self.pro.skills) + "\n"
		ret += str(self.pro.description()) + "\n"
		ret += "Testing Modifiers:" + "\n"
		ret += str(self.pro.getMods()) + "\n"
		return ret
class storyEvent(baseEvent):
	def __init__(self,protag,recurring):
		#protag.description()
		self.events = recurring
		self.pro = protag
		#The self contained story of an individual event
		#Should always be overridden
	def exeStory(self):
		raise interfaceError("exeStory is not overridden")
		#Calls a sequence of events for every story event.
		#Should not normally be overridden.
	def story(self):
		self.events.exeStory();
		self.exeStory();
class repeatedEvent(baseEvent):
	def exeStory(self):		
		self.play();
		self.train();
	def play():
		raise interfaceError("play is not overridden")
	def train():
		raise interfaceError("play is not overridden")
