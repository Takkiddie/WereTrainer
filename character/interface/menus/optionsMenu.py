import sys, pygame

#Has all of the information about the window
#Each Menu will have it's own object
class option:
    def __init__(self,text,pos,textstr):
        self.text = text
        self.pos = pos
        self.tpos = pos.move(3,3)
        self.textstr = textstr
class optionsMenu:
    def __init__(self,screen,winDisp):
        self.winDisp = winDisp
        self.size = width, height = 1000, 540
        self.white = 255, 255, 255
        self.linelen = 60
        self.screen = screen
		#totally arbitrary, but should be at least the button's height plus some.
        self.lineHeight = 43
        self.font = pygame.font.Font(None, self.lineHeight)
        self.background = pygame.image.load('werebutton.png')
    def collide(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : 
                x, y = event.pos
                for opp in self.options:
                    if opp.pos.collidepoint(x, y):
                        self.winDisp.chosen = opp.textstr
                        print(opp.textstr)
                        return
    def displayText(self):
        self.options = []
        dispStr = self.winDisp.options
        self.text = self.font.render(self.winDisp.dispString, 1, (10, 10, 10))
		#301 and 33 are the size of the button right now.
        self.textpos = pygame.Rect(100,100,301,33)
        #setting base position
		#Make screen white
        self.screen.fill(self.white)
        i = 0
        while i < len(dispStr):
            pos = self.textpos.move(0,self.lineHeight*(i))
            text = self.font.render(dispStr[i], 1, (10, 10, 10))            
            self.options.append(option(text,pos,dispStr[i]))
            self.screen.blit(self.background,self.options[i].pos)
            self.screen.blit(self.options[i].text,self.options[i].tpos)
            i = i+1

    def menu(self):
        self.collide()
        self.displayText()
        pygame.display.flip()
