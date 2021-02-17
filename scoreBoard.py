# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:11:39 2019

@author: Chloe
"""
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 2, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 2, 1, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

def scoreBoard(board):
    """
    Takes as argument a list 'board' representing the Othello board and returns
    an integer corresponding to the difference of the number of player1's and
    player2's counters. Positive scores indicate an advantage of player1, while
    negative scores indicate an advantage of player2
    
    Parameters
    ----------
    board : The Othello board as it looks in the current state of play
    
    Returns
    -------
    x + y : The total score of each players counters
    
    Example
    -------
    This will return a score of 7
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 2, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 2, 1, 0, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]] 
    
    """
    x = 0
    y = 0
    for i in board:
        for j in i:
            if j == 1:
                x += 1
            elif j == 2:
                y -= 1
    
    return x + y

print(scoreBoard(board))