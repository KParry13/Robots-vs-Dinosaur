import random
from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = 'Rebelbot'
        self.health = 100
        self.active_weapon = random.choice(Weapon([self.weapon.name]))
        
        

    def attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print ('Rebelbot uses his ax and does damage of 30!')
    

