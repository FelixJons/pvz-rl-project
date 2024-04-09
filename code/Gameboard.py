import numpy as np
import pygame
import h5py


plant_types = [[10,2,5], [5,4,5], [1,1,1] ] #hp, dmg, cost. 
zombie_types = [[10,2,1], [5,5,1],[1,1,1] ] #hp, dmg, speed. 
 
class Zombie:
    def __init__(self,hp,dmg,speed,position):
        self.hp = hp
        self.dmg = dmg 
        self.speed = speed
        self.position = position
        self.alive = 1

    def move(self):
        self.position -= self.speed

    def update_hp(self,dmg_taken):
        self.hp -= dmg_taken
        if self.hp <= 0 : 
            self.alive = 0

class Plant: 
    def __init__(self,hp,dmg,position):
        self.hp = hp
        self.dmg = dmg 
        self.position = position
        self.alive = 1

    def update_hp(self,dmg_taken):
        self.hp -= dmg_taken
        if self.hp <= 0 : 
            self.alive = 0

    

class PvZGameBoard: 

   def __init__(self,N_row,N_col,agent,stochastic_prob):
        
        self.N_row=N_row
        self.N_col=N_col
        self.board= np.zeros((N_row,N_col))

        

    
