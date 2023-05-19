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

#dimentions of game window
WIDTH = 1500 #width of game window
HEIGHT = 50 #width of game window
FPS = 30 #frames per second

#initialise pygame, sound and create window using dimetions above
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #display
pygame.display.set_caption("Big Balls") #game title
clock = pygame.time.Clock() #setting the clock

#RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
player = Player()
all_sprites.add(player)

#game loop
running = True
while running:
    #keep checking right speed
    clock.tick(FPS)
    #rerender#
    #Processes inputs
    for event in pygame.event.get():
        #check for quit
        if event.type == pygame.QUIT:
            running = False
    #UPDATE
    all_sprites.update()
    #draw / render screen
    screen.fill(black)
    all_sprites.draw(screen)
    #'after' drawing everthing, flip the display
    pygame.display.flip()


pygame.quit()






