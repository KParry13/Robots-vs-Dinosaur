from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.active_weapon = Weapon

    def __init__(self,name):
        self.name = name
        name = input('Name your robot: ')
        print ({name}' is your robot.')
        

    def attack(self,dinosaur):
        pass

