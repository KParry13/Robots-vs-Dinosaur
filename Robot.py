import random
from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = 'Rebelbot'
        self.health = 100
        self.weapon_name = ['blade', 'chainsaw', 'bow and arrow']
        self.active_weapon = Weapon(30)
        
        

    def attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print ('Rebelbot uses his', (random.choice(self.weapon_name)), 'and does damage of 30!')
    

