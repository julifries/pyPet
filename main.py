from helper import *
import pygame
from pygame.locals import *




class Button ():
    def __init__(self,name,x,y, image,scale):
        self.name=name
        width = image.get_width()
        height= image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        pos=pygame.mouse.get_pos()
        
        
        #check mouseover and clicked connections
        if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked ==False:
                        self.clicked = True
                        print('CLICKED')
                        action=True
        if pygame.mouse.get_pressed ()[0]==0:
                self.clicked = False
        #draw button on screen
        screen.blit(self.image,((self.rect.x),(self.rect.y)))

        return action
    




WIDTH = 2000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pyPet by Julia")
background_colour= (221,221,221)
screen.fill(background_colour)






#pics
exercise_img = pygame.image.load('buttons/exercise.png').convert_alpha()
feed_img = pygame.image.load('buttons/feed.png').convert_alpha()
love_img = pygame.image.load('buttons/love.png').convert_alpha()
sleep_img = pygame.image.load('buttons/sleep.png').convert_alpha()


exercise_button = Button('exercise',0,HEIGHT*0.75,exercise_img,0.75)
feed_button = Button('feed',WIDTH*0.25,HEIGHT*0.75,feed_img,0.75)
sleep_button = Button('sleep',WIDTH*0.5,HEIGHT*0.75,sleep_img,0.75)
love_button = Button('love',WIDTH*0.75,HEIGHT*0.75,love_img,0.75)


#sprites
egg_img=pygame.image.load('petSprites/egg.png').convert_alpha()
baby_img=pygame.image.load('petSprites/baby.png').convert_alpha()
child_img=pygame.image.load('petSprites/child.png').convert_alpha()
teenager_img=pygame.image.load('petSprites/teenager.png').convert_alpha()
adult_img=pygame.image.load('petSprites/adult.png').convert_alpha()
senior_img=pygame.image.load('petSprites/senior.png').convert_alpha()


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

def readButtons():
    if exercise_button.draw():
        print("exercise")
        newPet.goExercise()
    if feed_button.draw():
        print("feed")
        newPet.goEat()
    if sleep_button.draw():
        print("sleep")
        newPet.goSleep()
    if love_button.draw():
        print("love") 
        newPet.giveLove()



while gameIsRun:
    pygame.display.update()
    readButtons()
        
    for event in pygame.event.get(): #quit game
        if event.type == pygame.QUIT:
            gameIsRun = False
                        

#TO DO

#TEENAGER
#ADULT
#SENIOR
#ONE SPRITE PER EACH
