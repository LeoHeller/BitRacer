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

        #Colors
        global black, white, red, blue, grey, green, hotpink, lightgreen, light_grey 
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)
        blue = (20, 20, 255)
        grey = (55, 55, 55)
        green = (0,255,0)
        hotpink = (255,96,96) 
        lightgreen = (96,255,96)
        light_grey = (145,145,145)

        #extra variables
        pause = False
        cwd = os.path.dirname(sys.argv[0])
        global guy_width
        guy_width = 73
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('BitRacer')
        self.clock = pygame.time.Clock()
        

        #importing images
        global bgImg, guyImg, trashImg
        bgImg = pygame.image.load(cwd+'\\road.png')
        guyImg = pygame.image.load(cwd+'\\guy.png')
        trashImg = pygame.image.load(cwd+'\\trash.png')

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
        
        

    def true():
        while true:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
            self.gameDisplay.fill(light_grey)
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
            self.gameDisplay.fill(light_grey)
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
        
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
            self.gameDisplay.fill(light_grey)
            largeText = pygame.font.Font('freesansbold.ttf',100)
            TextSurf, TextRect = self.text_objects("Bitracer", largeText)
            TextRect.center = ((self.display_width/2),(self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)
            
            #adds buttons to intro screen
            self.button("START",150,450,100,50,lightgreen,self.game_loop)
            self.button("Exit",550,450,100,50,hotpink, self.quit_game)
            self.button("Load Game",350,450,125,50,lightgreen,self.load)
            #finds mouse position
            mouse = pygame.mouse.get_pos()
            
            self.gameDisplay.blit(TextSurf, TextRect)
            #updates screen
            pygame.display.update()
            self.clock.tick(60)



    def game_loop(self):
        
        global pause

        global x
        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)

        x_change = 0

        trash_start_x = random.randrange(0, self.display_width)
        trash_start_y = -500
        global trash_speed
        trash_speed = 7
        #block_width = 100
        #block_height = 100

        gameExit = False
        global count
        count = 0

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

            x += x_change

            self.gameDisplay.blit(bgImg,(0,0))
            self.trash(trash_start_x, trash_start_y)
            trash_start_y += trash_speed
            trash_speed = trash_speed + 0.001
            

            

            self.guy(x,y)
            self.trash_dodged(count)
            if x > self.display_width - guy_width or x < 0:
                true()
            if trash_start_y > self.display_height:
                trash_start_y = 0 - 62
                trash_start_x = random.randrange(62, self.display_width - 62)
                count += 1
            
            if y < trash_start_y + 62:
                if x > trash_start_x and x < trash_start_x + 62 or x + guy_width > trash_start_x and x + guy_width < trash_start_x + 62:
                    true()
            
            pygame.display.update()
            self.clock.tick(60)


        
    def save(self):
        cwd = os.path.dirname(sys.argv[0])

        with open(cwd+"\\text.txt", "w") as f:
            print(count,"\n", x,"\n",trash_speed,"\n",file = f)    

    def load(self):
        cwd = os.path.dirname(sys.argv[0])

        with open(cwd+"\\text.txt", "r") as f:
            print(map(float, f))
                

        

#Game_1 = Game(3,500,10)

#print(Game_1.dodged, Game_1.x, Game_1.trash_speed)
