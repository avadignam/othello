# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:50:35 2019

@author: Chloe
"""

def newGame(player1,player2):
    """
    Parameters
    ----------
    player1 : a string indicating who the first player is, is equal to 'C' if 
              this player is a computer
    player2 : same as above
    
    Returns
    -------
    game : a dictionary consisting of player1, player2, which players turn is 
           next, and a fresh game board
           
    """
    game = {
            'player1' : '{}'.format(player1),
            'player2' : '{}'.format(player2),
            'who' : 1,
            'board' : [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 2, 0, 0, 0],
                       [0, 0, 0, 2, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
            }
    
    return game

newGame(player1, player2)