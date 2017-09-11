# 1. make a class that has the atributes of dodged count, position of x and y, trash speed, and class name
# 2. def save (writes the class to a file)
# 3. add save button to pause screen
# 4. add button on intro screen to go to a load save screen.
# 5. add buttons for loading the game
import os
import sys
import pygame
import time
import random

class Game:
    def __init__(self, display_width, display_height):
        
        
        self.display_width = display_width
        self.display_height = display_height
        self.intro = True

        #Colors
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.blue = (20, 20, 255)
        self.grey = (55, 55, 55)
        self.green = (0,255,0)
        self.hotpink = (255,96,96) 
        self.lightgreen = (96,255,96)
        self.light_grey = (145,145,145)
        self.guy_x = (display_width*0.45)
        #extra variables
        self.pause = False
        cwd = os.path.dirname(sys.argv[0])
        self.guy_width = 73
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('BitRacer')
        self.clock = pygame.time.Clock()
        
        

        #importing images
        self.bgImg = pygame.image.load(cwd+'\\road.png')
        self.guyImg = pygame.image.load(cwd+'\\guy.png')
        self.trashImg = pygame.image.load(cwd+'\\trash.png')
        self.init()
        

    def init(self,init = True):
        if init == True:   
            self.guy_x = (self.display_width * 0.45)
            self.trash_speed = 7
            self.count = 0
        self.guy_y = (self.display_height * 0.8)

        

        self.trash_start_x = random.randrange(0, self.display_width)
        self.trash_start_y = -500
        self.gameDisplay.blit(self.bgImg,(0,0))
        #block_width = 100
        #block_height = 100

        self.gameExit = False
        
    def start_game(self):
        self.init()
        self.game_loop()     

    def trash_dodged(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, black)
        self.gameDisplay.blit(text, (0,0))

    def trash(self,trash_x,trash_y):
        self.gameDisplay.blit(trashImg,(trash_x,trash_y))
    

    def guy(self,x,y):
        self.gameDisplay.blit(guyImg,(x,y))

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self.display_width/2), (self.display_height/2))
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        self.game_loop()
        
        

    def crash(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
            self.gameDisplay.fill(self.light_grey)
            largeText = pygame.font.Font('freesansbold.ttf',100)
            TextSurf, TextRect = self.text_objects("You Crashed", largeText)
            TextRect.center = ((self.display_width/2), (self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            #adds buttons to intro screen
            self.button("Play again",150,450,150,50,lightgreen,self.game_loop)
            self.button("Exit",550,450,100,50,hotpink,self.quit_game)
            #finds mouse position
            mouse = pygame.mouse.get_pos()
            
            self.gameDisplay.blit(TextSurf, TextRect)
            #updates screen
            pygame.display.update()
            self.clock.tick(60)


    def quit_game(self):
        pygame.quit()
        quit()

    def button(self,msg,x,y,w,h,color,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        ax = x-10
        ay = y-10
        aw = w+20
        ah = h+20
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, color,(ax,ay,aw,ah))
            if click[0] == 1 and action != None:
                self.intro = False
                action()
                

                
        else:
            pygame.draw.rect(self.gameDisplay, color, (x,y,w,h))
        
        smallText = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = self.text_objects(msg, smallText)
        TextRect.center = ((x+(w/2)),y+(h/2))
        self.gameDisplay.blit(TextSurf, TextRect)





    def unpause(self):
        global pause
        pause = False

    def paused(self):
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
            self.gameDisplay.fill(self.light_grey)
            largeText = pygame.font.Font('freesansbold.ttf',100)
            TextSurf, TextRect = self.text_objects("Bitracer", largeText)
            TextRect.center = ((self.display_width/2), (self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            #adds buttons to intro screen
            self.button("Continue",150,450,150,50,lightgreen,self.unpause)
            self.button("Exit",550,450,100,50,hotpink,self.quit_game)
            self.button("Save",350,450,125,50,hotpink,self.save)        
            #finds mouse position
            mouse = pygame.mouse.get_pos()
            
            self.gameDisplay.blit(TextSurf, TextRect)
            #updates screen
            pygame.display.update()
            self.clock.tick(60)


    def game_intro(self):
        
        #intro = True

        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
            self.gameDisplay.fill(self.light_rey)
            largeText = pygame.font.Font('freesansbold.ttf',100)
            TextSurf, TextRect = self.text_objects("Bitracer", largeText)
            TextRect.center = ((self.display_width/2),(self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)
            
            #adds buttons to intro screen
            self.button("START",150,450,100,50,lightgreen,self.start_game)
            self.button("Exit",550,450,100,50,hotpink, self.quit_game)
            self.button("Load Game",350,450,125,50,lightgreen,self.load)
            #finds mouse position
            mouse = pygame.mouse.get_pos()
            
            self.gameDisplay.blit(TextSurf, TextRect)
            #updates screen
            pygame.display.update()
            self.clock.tick(60)



    def game_loop(self, init=True):
        while not self.gameExit:
            x_change = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #print(str(event.type))
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_p:
                        pause = True
                        self.paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            self.guy_x += x_change
            #print(str(self.x))
            self.trash(self.trash_start_x, self.trash_start_y)
            self.trash_start_y += trash_speed
            trash_speed = trash_speed + 0.001
            self.guy(self.guy_x,self.guy_y)
            self.trash_dodged(count)
            if self.guy_x > self.display_width - guy_width or self.guy_x < 0:
                self.crash()
            if self.trash_start_y > self.display_height:
                self.trash_start_y = 0 - 62
                self.trash_start_x = random.randrange(62, self.display_width - 62)
                count += 1
            
            if y < self.trash_start_y + 62:
                if self.guy_x > self.trash_start_x and self.guy_x < self.trash_start_x + 62 or self.guy_x + guy_width > self.trash_start_x and self.guy_x + guy_width < self.trash_start_x + 62:
                    self.crash()
            
            pygame.display.update()
            self.clock.tick(60)


        
    def save(self):
        cwd = os.path.dirname(sys.argv[0])

        with open(cwd+"\\text.txt", "w") as f:
            print(str(count)+"\n"+str(self.guy_x)+"\n"+str(trash_speed)+"\n",file = f)    

    def load(self):
        cwd = os.path.dirname(sys.argv[0])

        with open(cwd+"\\text.txt", "r") as f:
            contents = f.readlines()
            contents =[l.strip() for l in contents]
            count = int(contents[0], base = 10)
            self.guy_x = float(contents[1])
            self.trash_speed = float(contents[2])
            #self.game_loop(False)
            print(contents)
            #intro = False    

        

#Game_1 = Game(3,500,10)

#print(Game_1.dodged, Game_1.x, Game_1.trash_speed)
