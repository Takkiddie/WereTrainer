import sys, pygame
import _thread
import time
from talkMenu import *
from optionsMenu import *

#This is a static class. There is only one instance
class display:
   _instance = None
   dispString = "default"
   dispPortrate = "1Blank.png"
   options = ["default","dofault"]
   #Selection choice out of options
   chosen = ""
   dispWhat = "talk"
   paused = 0
   starting = True;
   #Globally show if window is still running.
   running = True;

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
      #Waits a moment when starting up. Breaks race conditions somewhere.
	  #This solves the strange wait on start-up. I'm not sure why.
      if self.starting:
         time.sleep(1)
         self.starting = False;
      while self.paused and self.running:
         pass
      #if the window is closed. Stop the program entirely.
      if not self.running:
         sys.exit()

#Has all of the information about the window
#Each Menu will have it's own object
class myWindow:
    def __init__(self):
        self.winDisp = display()
        self.size = width, height = 1000, 600
        self.white = 255, 255, 255
        self.linelen = 60
    def initiateWindow(self):
       pygame.init()
       self.screen = pygame.display.set_mode(self.size)
       talk = talkMenu(self.screen,self.winDisp)
       options = optionsMenu(self.screen,self.winDisp)
       i = 1
       while self.winDisp.running:
            if self.winDisp.dispWhat == "talk":
                self.winDisp.running = talk.menu()
            elif self.winDisp.dispWhat == "options":
                self.winDisp.running = options.menu()
            
mywind = myWindow()
disp = display()
_thread.start_new_thread(mywind.initiateWindow,())
