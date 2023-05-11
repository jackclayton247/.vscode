#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      TWY-6451
#
# Created:     09/05/2023
# Copyright:   (c) TWY-6451 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Pygame template - skeleton for a new pygame
import pygame  #pygame library
import random  #random library

#RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#dimentions of game window
WIDTH = 360 #width of game window
HEIGHT = 480 #width of game window
FPS = 30 #frames per second

#initialise pygame, sound and create window using dimetions above
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #display
pygame.display.set_caption("Big Balls") #game title
clock = pygame.time.Clock() #setting the clock

#game loop
running = True
while running:
    #keep checking right speed
    clock.tick(FPS)
    #process inputs (events)
    #update variables
    #rerender

#draw / render screen
screen.fill(black)
#'after' drawing everthing, flip the display
pygame.display.flip()

for event in pygame.event.get():
    #check for quit
    if event.type == pygame.QUIT:
        running = False


















