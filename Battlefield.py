from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the battlefield, where we find out if Robots will destoy the dinosaurs into extinction once and for all.')
        print('Or will the dinosaurs tear the robots apart screw by screw?')
        print('Let the battle begin!')
        print ('')


    def battle_phase(self):
        # Dinosaur.health = Dinosaur.health - Robot.attack
        # Robot.health = Robot.health - Dinosaur.attack
        while self.dinosaur.health > 0 and self.robot.health >0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
            print ('')
            
            if self.dinosaur.health >= self.robot.health:
                print(f'Rebelbot health is down to {self.robot.health}')
                print ('Oh! Nice hit!')
                print ('')
            elif self.dinosaur.health <= self.robot.health:
                print (f'Shelbausaurs health is down to {self.dinosaur.health}')
                print('Ouch! That had to hurt!')
                print ('')

         


    def display_winner(self):
        if self.dinosaur.health == 0:
            print ("Congratualtions! Dinosaurs tore the robots apart!")
        elif self.robot.health == 0:
            print ("Congratulations! Robots have slayed the Dinosaurs into extinction!")
        

    
