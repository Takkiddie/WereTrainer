from freetime import *
from lessons import *
from display import *
from playMenu import *
from trainMenu import *
		
#Executes every turn.
class recurring(repeatedEvent):
	def __init__(self,protag):
		self.pro = protag;
		self.freeTime = {}
		self.freeTime["Play Fetch"] = playFetch(self.pro);
		self.freeTime["Massage"] = massage(self.pro);
		self.freeTime["Bath"] = bath(self.pro);
		self.freeTime["Park"] = park(self.pro);
		self.freeTime["Watch Performance"] = watchPerformance(self.pro);
		self.freeTime["Watch News"] = news(self.pro);opponents
		self.freeTime["Watch opponents"] = opponents(self.pro);
		self.lesson = {}
		self.lesson["Strength"] = teachStrength(self.pro);
		self.lesson["Constitution"] = teachConstitution(self.pro);
		self.lesson["Speed"] = teachSpeed(self.pro);
		self.lesson["Submission"] = teachSubmission(self.pro);
		self.lesson["Patience"] = teachPatience(self.pro);
		self.lesson["Memory"] = teachMemory(self.pro);
		self.lesson["Posturing"] = teachPosturing(self.pro);
		self.lesson["Dignity"] = teachDignity(self.pro);
		self.lesson["Grace"] = teachGrace(self.pro);
	#maybe refactor?
	def play(self):
		menu = playMenu()
		activity = menu.play(self.freeTime.keys())
		if(activity in self.freeTime):
			disp(self.freeTime[activity].exeStory())
		else:
			disp("not an activity: "+activity);		
	def train(self):
		menu = trainMenu()
		lesson = menu.train(self.lesson.keys())
		#Also do one for skills
		#lesson = input("Pick a Skill To train: ")
		if(lesson in self.lesson):
			disp(self.lesson[lesson].exeStory())
		else:
			disp("not a lesson: "+lesson);		
