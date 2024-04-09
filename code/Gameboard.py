import numpy as np
import pygame
import h5py


plant_types = [[10,2,5], [5,4,5], [1,1,1] ] #hp, dmg, cost. 
zombie_types = [[10,2,1], [5,5,1],[1,1,1] ] #hp, dmg, speed. 
 
class Zombie:
    def __init__(self,hp,dmg,speed,position:list):
        self.hp = hp
        self.dmg = dmg 
        self.speed = speed
        self.position = position
        self.alive = 1


    def move(self):
        self.position[1] -= self.speed

    def update_hp(self,dmg_taken):
        self.hp -= dmg_taken
        if self.hp <= 0 : 
            self.alive = 0

class Plant: 
    def __init__(self,hp,dmg,position:list):
        self.hp = hp
        self.dmg = dmg 
        self.position = position
        self.alive = 1

    def update_hp(self,dmg_taken):
        self.hp -= dmg_taken
        if self.hp <= 0 : 
            self.alive = 0

    

class PvZGameBoard: 

    def __init__(self,N_row,N_col):
        
        self.N_row=N_row
        self.N_col=N_col
        self.Zombies_list = []
        self.Plants_list = []
        self.current_sun = 5
        self.plants_grid = np.zeros((N_row,N_col))
        self.gameover = 1



    def spawn_zombie(self,lane,zombie_type):
        zombie_specs = zombie_types[zombie_type]  #hp, dmg, speed. 
        zombie = Zombie(zombie_specs[0],zombie_specs[1],zombie_specs[2],[lane,self.N_col])
        self.Zombies_list.append(zombie)

    def plant_plant(self,position:list,plant_type):
        plant_specs = plant_types[plant_type] #hp, dmg, speed. 
        plant = Plant(plant_specs[0],plant_specs[1],position)
        self.Plants_list.append(plant)
        self.current_sun -= plant_specs[2]
        self.plants_grid[position[0],position[1]] = 1

    def update_poitions(self):
        for zombie in self.Zombies_list: 
            if self.plants_grid[zombie.position[0],zombie.position[1]]:
                pass #om zombien är på samma position som plantan, så ska plantan ta dmg. 
                #man borde även kolla om plantan dör, för isf ska den raderas från self.plants_grid (ersätt med 0)
                # man kan använda plant.alive för att veta om den är fortfarande vid liv. 
            else:
                zombie.move()
                if zombie.position[1] <= 0: 
                    self.gameover = 0
                    break

    def update_hp(self):
        pass #här ska alla zombies som är längst in ta dmg. problem: identifiera zombies som är längst in,
            # och ta dmg från bara respektive lane
            