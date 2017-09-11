import pygame
import time
import random
import os
import sys
import grape

pygame.init()


display_width = 800
display_height = 600

game = grape.Game(display_width, display_height)



game.game_intro()
game.game_loop()

pygame.quit()
quit()