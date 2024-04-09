import numpy as np 
import Gameboard as gb
import Agent

rows = 3
cols = 7

waves = [ [ [0,1] , [1,1] ,[2,0]], [ [0,1] , [1,1] ,[2,0] ] ] #förbestämda zombies, lista av waves och varje wave är lista av zombies. 
# detta motsvarar alltså två waves med 3 zombies var. första siffran är vilken lane den ska spawnas på, och andra siffran är vilken typ av zombie.


gameboard = gb.PvZGameBoard(rows,cols)
wave_nr = 0
while gameboard.gameover: 

    for input in waves[wave_nr]: 
        gameboard.spawn_zombie(input[0],input[1])
    
    wave_nr += 1

    gameboard.update_poitions()
    gameboard.update_hp()