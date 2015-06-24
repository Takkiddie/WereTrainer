import sys, pygame, os

#Has all of the information about the window
#Each Menu will have it's own object
class talkMenu:
    def __init__(self,screen,winDisp):
        self.winDisp = winDisp
        self.size = width, height = 1000, 540
        self.white = 255, 255, 255
        self.linelen = 100
        self.screen = screen
        lineHeight = 36

        self.font = pygame.font.Font(None, 20)
        self.font = pygame.font.SysFont("timesnewroman", 20)

        #pygame.font.match_font("timesnewroman")
        #print(pygame.font.get_fonts())
        		
        self.text = self.font.render(self.winDisp.dispString, 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos = self.textpos.move(100,100)
        self.textpos2 = self.textpos.move(0,lineHeight)
        self.textpos3 = self.textpos.move(0,lineHeight*2)
    def collide(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN : 
                x, y = event.pos
                self.winDisp.paused = 0
    def breakText(self,str):
        dispLen = len(str)
        str = str[0:dispLen-1]
        ret = ["","",""]
        if dispLen > self.linelen*2:
            ret[2] = str[self.linelen*2:dispLen]
            ret[1] = str[self.linelen:self.linelen*2]
            ret[0] = str[0:self.linelen]
        elif dispLen > self.linelen:
            ret[1] = str[self.linelen:dispLen]
            ret[0] = str[0:self.linelen]
        else:
            ret[0] = str
        return ret
    def displayText(self):
        dispStr = self.breakText(self.winDisp.dispString)

        self.screen.fill(self.white)
        #Displaying Text
        self.text = self.font.render(dispStr[0], 1, (10, 10, 10))
        self.text2 = self.font.render(dispStr[1], 1, (10, 10, 10))
        self.text3 = self.font.render(dispStr[2], 1, (10, 10, 10))
        self.screen.blit(self.text, self.textpos)
        self.screen.blit(self.text2, self.textpos2)
        self.screen.blit(self.text3, self.textpos3)
    def menu(self):
        self.collide()
        self.displayText()
        pygame.display.flip()
