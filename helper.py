from enum import Enum, auto
import time


class Stage(Enum):
  Egg = auto()
  Baby = auto()
  Child = auto()
  Teenager = auto()
  Adult = auto()
  Senior = auto ()

stages = [Stage.Egg,Stage.Baby,Stage.Child,Stage.Teenager,Stage.Adult,Stage.Senior]






class Food:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

class Tamagotchi:
    #init method for new pet
    def __init__(self,name):
        self.name = name #player chooses a name
        #default init values
        self.stage = Stage.Baby #age for tamagotchi
        self.hunger = 50
        self.happiness = 50
        self.exercise = 50
        self.health = 50
        self.sleep = 50
        self.level = 0
        self.index=0
        #perhaps add race
        
    def levelUp(self):
        if self.level>=100:
            self.stage=stages[self.index+1]
            self.level-=100
    
        
    #INCREASING STATS METHODS
    def goEat (self):
         if(self.hunger<100):
             self.hunger +=1
             self.level+=1
    
    def giveLove(self):
        if(self.happiness<100):
            self.happiness+=1
            self.level+=1

    
    def goExercise (self):
         if(self.exercise<100):
            self.sleep +=1
            self.level+=1

    
    def goSleep (self):
         if(self.sleep<100):
            self.sleep +=1
            self.level+=1

        
    def makeHealthy (self):
        if (self.exercise>=50 and self.sleep>=50 and self.happiness>=50 and self.health<100):
            self.health +=1
        
  
        
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
    
    
    def die(self):
        return self.health <= 0
    




    
 
