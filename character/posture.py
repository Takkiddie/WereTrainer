#Global constants
#moods
nervous = "nervous"
excited = "excited"
sad = "sad"
happy = "happy"
relaxed = "relaxed"
aggressive = "aggressive"
passive = "passive"
dominant = "dominant"
#skills
obedience = "obedience"
submission = "submission"
patience = "patience"
memory = "memory"
athletics = "athletics"
strength = "strength"
constitution = "constitution"
speed = "speed"
performance = "performance"
posturing = "posturing"
dignity = "dignity"
grace = "grace"



class posture( object ):
   #posture class, based on mood and other things.
   #you'll have to implement methods in children.
   def d1( self ):
      raise NotImplementedError( "Implement d1" )
   def d2( self ):
      raise NotImplementedError( "Implement d2" )
   def d3( self ):
      raise NotImplementedError( "Implement d3" )
   def d4( self ):
      raise NotImplementedError( "Implement d4" )
   def d5( self ):
      raise NotImplementedError( "Implement d5" )
   def d6( self ):
      raise NotImplementedError( "Implement d6" )


class nervousPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(nervousPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Standing alert"
   def d2( self ):
      return "twitch atop his head."
   def d3( self ):
      return "With every shallow breath he carefully sniffs the air."
   def d4( self ):
      return "He keeps a fair distance and drops his gaze anytime you look at him."
   def d5( self ):
      return "When you leave him he usually starts pacing."
   def d6( self ):
      return "When he sits, he gnaws relentlessly on"

class excitedPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(excitedPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Atop his head"
   def d2( self ):
      return "prick up at any sound."
   def d3( self ):
      return "He breathes quickly, almost bursting with energy."
   def d4( self ):
      return "He glances at you any time you move."
   def d5( self ):
      return "You've caught him digging at the floor and walls anytime he forgets you're looking."
   def d6( self ):
      return "When he sits, he gnaws relentlessly on"

class sadPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(sadPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "On his head"
   def d2( self ):
      return "lay flat against his skull."
   def d3( self ):
      return "Heavy sighs occationally interrupt his otherwise quiet breathing."
   def d4( self ):
      return "Content to pout, he largely ignores you."
   def d5( self ):
      return "He just lays and looks out the window when you leave him alone."
   def d6( self ):
      return "Occationally he'll bat at"

class happyPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(happyPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Up and alert"
   def d2( self ):
      return "prick up at interesting sounds."
   def d3( self ):
      return "He sniffs the air diligently, exploring the world with his nose."
   def d4( self ):
      return "He bounces when he walks, oblivious to you."
   def d5( self ):
      return "When left alone, he'll play anything available."
   def d6( self ):
      return "He particularly likes chewing on"

class relaxedPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(relaxedPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Low on his head"
   def d2( self ):
      return "lay like limp rags."
   def d3( self ):
      return "His steady, deep breaths come back out at heavy sighs."
   def d4( self ):
      return "He dosen't much notice you as he mozys around the room."
   def d5( self ):
      return "He doses off if you leave him alone for long."
   def d6( self ):
      return "Every once in a while, he'll nibble on"

class aggressivePosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(aggressivePosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Plastered down against his head"
   def d2( self ):
      return "alomst vanish into his fur"
   def d3( self ):
      return "Low growls occationally punctuate his heavy breathing."
   def d4( self ):
      return "Keeing his distance, he glares any time you make eye contact."
   def d5( self ):
      return "When left alone, he stalks back and forth."
   def d6( self ):
      return "He activly tries to rip appart"

class passivePosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(passivePosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Flat on his head"
   def d2( self ):
      return "only stand in reponse to interesting sounds."
   def d3( self ):
      return "His steady breating blend into the background."
   def d4( self ):
      return "He stays close to you and looks at you for instruction."
   def d5( self ):
      return "When you have to go, he looks out the window and patiently awaits your return."
   def d6( self ):
      return "He'll also chew on"

class dominantPosture(posture):
   _instance = None
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(dominantPosture, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def d1( self ):
      return "Atop his head"
   def d2( self ):
      return "stand upright."
   def d3( self ):
      return "He puffs out his chest to look larger, and every steady breath reminds you of his presence."
   def d4( self ):
      return "He struts with his head up and meets your gaze with a challenging grin."
   def d5( self ):
      return "He spends his alone time grooming and"
   def d6( self ):
      return "occasionally chewing on"

def poses(mood):
   if(mood == nervous):
      ret = nervousPosture()
   elif(mood == excited):
      ret = excitedPosture()
   elif(mood == sad):
      ret = sadPosture()
   elif(mood == happy):
      ret = happyPosture()
   elif(mood == relaxed):
      ret = relaxedPosture()
   elif(mood == aggressive):
      ret = aggressivePosture()
   elif(mood == passive):
      ret = passivePosture()
   elif(mood == dominant):
      ret = dominantPosture()
   return ret;


