import sys
sys.path.insert(0, 'character')
from were import *
from recurring import *
from display import *
from displayFile import *
from options import *

TrainAnswer = 1

class wereStoryEvent(storyEvent):
	def __init__(self):
		self.pro = myWere()
		#Periodic activities
		rec = recurring(self.pro);
		self.events = rec
		#self.pro.description()

#First event, will not act as a normal day, it will just execute
class startstory():
	def __init__(self):
		self.pro = myWere()
	def story(self):
		fileLoad("day0.txt");
		opps = optionMenu();
		op = opps.options(["Yes","No","Why?"]);
		if op == "Why?":
			fileLoad("day0Why.txt");
			#Set flag "Stacks"
			self.pro.flags[TrainAnswer] = "Why?"
			op = opps.options(["Yes","No"]);
		else:
			self.pro.flags[TrainAnswer] = "noask"			
		if op == "Yes":
			fileLoad("day0yes.txt");
		elif op == "No":
			fileLoad("day0no.txt");
			return "The end."
		

#The first day of twenty
class day1(wereStoryEvent):
	def exeStory(self):
		fileLoad("day1.txt")		

class day2(wereStoryEvent):
	def exeStory(self):
		#Read flag 
		if self.pro.flags[TrainAnswer] == "Why?":
			fileLoad("day2why.txt");
		else:
			fileLoad("day2.txt");

class day3(wereStoryEvent):
	def exeStory(self):
		fileLoad("day3.txt");
		self.pro.mood.changeMood(passive)
		self.pro.mood.changeMood(happy)

class day4(wereStoryEvent):
	def exeStory(self):
		testSkill = constitution
		disp("Testing skill:"+testSkill);
		if self.pro.skills[testSkill].mastery > 0:
				disp("pass")
		else:
				disp("fail")

