from helper import *
import pygame
from pygame.locals import *



WIDTH = 2000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pyPet by Julia")
background_colour= (221,221,221)
screen.fill(background_colour)


exercise_img = pygame.image.load('buttons/exercise.png').convert_alpha()
feed_img = pygame.image.load('buttons/feed.png').convert_alpha()
love_img = pygame.image.load('buttons/love.png').convert_alpha()
sleep_img = pygame.image.load('buttons/sleep.png').convert_alpha()





def every10SEC (pet):
        pet.starve()
        pet.getDepressed ()
        pet.destroyFitness ()
        pet.destroyHealth()
        pet.getTired()
    
    
    
    
    
    
newPet = Tamagotchi("Drago")
pygame.init()


#initilize pygame environment 
gameIsRun=True

#background and window configs





while gameIsRun:
        for event in pygame.event.get(): #quit game
                if event.type == pygame.QUIT:
                        gameIsRun=False
                        
        pygame.display.update()