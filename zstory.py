import sys
sys.path.insert(0, 'character')
sys.path.insert(0, 'character/engine')
sys.path.insert(0, 'character/interface')
sys.path.insert(0, 'character/interface/menus')

from were import *
from freetime import *
from storyEvents import *
from recurring import *
from display import *
from displayFile import *

events = [];

ending = None;

#events.append( startstory())
events.append( day1())
events.append( day2())
events.append( day3())
events.append( day4())

for event in events:
	ending = event.story()
	if ending != None:
		break;

#Display whatever the ending is
#This will get a lot more complex...
disp(str(ending))
disp("")

#Finish 'freetime' it's incomplete
#Also do different strings for levels of mastery of skills
#Do a story that's twenty units of time long (Months?)
#Submission should be locked at first (It will be akin to magic)
#Eventually load text from separate files.
#I need a game over script