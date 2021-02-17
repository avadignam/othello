# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:40:54 2019

@author: Chloe
"""

def loadGame():
    """
    Loads a pre-existing game from 'game.txt' to be played
    
    Returns
    -------
    d : A dictionary consisting of keys 'player1', 'player2', 'who', and
        'board' loaded from a file 'game.txt' 
        
    Raises
    ------
    FileNotFoundError : if the 'game.txt' file does not already exist
    ValueError : if the 'game.txt' file does exist but is of the wrong format
    """
    lines = []
    listlines = []
    d = {
            'player1' : None,
            'player2' : None,
            'who' : None,
            'board' : None
        }
    with open("game.txt", mode="rt", encoding="utf8") as f:
        f = f.read().splitlines()
        d['player1'] = f.pop(0)
        d['player2'] = f.pop(0)
        d['who'] = int(f.pop(0))
                
        d['board'] = [list(int(y) for y in (x.replace(",", "").replace(" ", ""))) for x in f]
        
    return d

print(loadGame())
            