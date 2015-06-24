import sys, pygame
import _thread
from talkMenu import *
from optionsMenu import *

class display:
   _instance = None
   dispString = "default"
   options = ["default","dofault"]
   #Selection choice out of options
   chosen = ""
   dispWhat = "talk"
   paused = 0
   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(display, cls).__new__(cls, *args, **kwargs)
      return cls._instance
   def __call__(self,str):
      self.dispString = str
      #Keeps the rest of the game paused while displaying options
      self.paused = 1
      dispWhat = "talk"
      if self.dispString == "\n" or self.dispString == "":
         self.paused = 0
      while self.paused:
         pass

#Has all of the information about the window
#Each Menu will have it's own object
class myWindow:
    def __init__(self):
        self.winDisp = display()
        self.size = width, height = 1000, 540
        self.white = 255, 255, 255
        self.linelen = 60
    def initiateWindow(self):
       pygame.init()
       self.screen = pygame.display.set_mode(self.size)
       talk = talkMenu(self.screen,self.winDisp)
       options = optionsMenu(self.screen,self.winDisp)
       i = 1
       while 1:
            if self.winDisp.dispWhat == "talk":
                talk.menu()
            elif self.winDisp.dispWhat == "options":
                options.menu()
mywind = myWindow()
disp = display()
_thread.start_new_thread(mywind.initiateWindow,())
