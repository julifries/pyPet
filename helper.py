from enum import Enum, auto
import time


class Stages(Enum):
  Egg = auto()
  Baby = auto()
  Child = auto()
  Teenager = auto()
  Adult = auto()
  Senior = auto ()



class Food:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

class Tamagotchi:
    #init method for new pet
    def __init__(self,name):
        self.name = name #player chooses a name
        #default init values
        self.stage = Stages.Baby #age for tamagotchi
        self.hunger = 100
        self.happiness = 100
        self.exercise = 100
        self.health = 100
        self.sleep = 100
        #perhaps add race
        
        
        
    #INCREASING STATS METHODS
    def eat (self,foodPoints):
        self.hunger += foodPoints
    
    def makeHappy(self,happyPoints):
        self.happiness+=happyPoints
    
    def exercise (self,isRunning):
          #for every second increase 
        while isRunning:
            self.sleep +=1
        
        
    def makeHealthy (self,healthPoints):
        if (self.exercise>=50 and self.sleep>=50 and self.happiness>=50):
            self.health +=1
        
    def sleep (self,isRunning):
        #for every second increase 
        while isRunning:
            self.sleep +=1
        
   #DECREASING STATS METHODS
    def starve(self):
        self.hunger-=1
   
    def getDepressed (self):
       self.happiness-=1
    
    def destroyFitness (self):
        self.exercise -=1
    
    def destroyHealth (self):
        self.health-=1
    
    def getTired (self):
        self.sleep -=1
       
    
    
 
