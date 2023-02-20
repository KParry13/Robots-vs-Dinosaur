from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        Robot.attack
        Dinosaur.attack


    def display_welcome(self):
        print('Welcome to the battlefield, where we find out if Robots will destoy the dinosaurs into extinction once and for all.')
        print('Or will the dinosaurs tear the robots apart screw by screw?')
        print('Let the battle begin!')

    def battle_phase(self):
        while Dinosaur.health > 0 and Robot.health >0:
            Robot.attack(-20)
            Dinosaur.attack(-25)
            
            if Dinosaur.health >= Robot.health:
                print(f'Rebelbot health is down to {Robot.health}')
                print ('Oh! Nice hit!')
            elif Dinosaur.health <= Robot.health:
                print (f'Shelbausaurs health is down to {Dinosaur.health}')
                print('Ouch! That had to hurt!')

         


    def display_winner(self):
        if Dinosaur.health == 0:
            print ("Congratualtions! Robots have slayed the Dinosaurs into extinction!")
        elif Robot.health == 0:
            print ("Congratulations! Dinosaurs tore the robots apart!")
        

    run_game()
