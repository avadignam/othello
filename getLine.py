# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:13:57 2019

@author: Chloe
"""
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0],
         [0, 1, 1, 1, 2, 1, 1, 1],
         [0, 2, 1, 2, 2, 0, 0, 0],
         [0, 0, 2, 1, 2, 0, 0, 0],
         [0, 2, 2, 2, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0]]
move = (3, 0)
dir = (0, -1)
who = 2

def getLine(board, who, pos, dir):
    """
    Finds a line in the chosen direction and returns the positions of the
    opponents counters if there
    
    Parameters
    ----------
    board : An array which represents the Othello game board as it is in its
            current state of play
    who : An integer, 1 or 2, indicating the player whos turn it is currently
    pos : A tuple of the form (r, c) with r and c being integers such that 
          0 <= r, c <= 7, corresponding to the indices of the board row and
          column, respectively
    dir : A tuple of the form (r, c) with r and c being integers such that
          -1 <= r, c <= 1, corresponding to the direction of the line
          
    Returns
    -------
    result : A list of the positions of the opponent's pieces on the board in 
             the direction of dir, which are on a continuous horizontal, 
             vertical, or diagonal line and end with a piece of the current
             player, who
             
    Examples
    --------
    >>>board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 2, 2, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        who = 1
        pos = (3, 6)
        dir = (0, -1)
        This should return the list [(3, 5), (3, 4), (3, 3)]
    >>>board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 2, 2, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        who = 1
        pos = (2, 5)
        dir = (1, -1)
        This should return an empty list
    
    """
    result = []
    p = pos
    q = (p[0]+dir[0], p[1]+dir[1]) #q is the next space in direction of dir
    if who == 1:
        a = 1
        b = 2
    elif who == 2:
        a = 2
        b = 1
        
    try:
        while board[q[0]][q[1]] == b: 
            q = (p[0]+dir[0], p[1]+dir[1])
            if board[q[0]][q[1]] != b: #if the next space is not occupied by the other persons counter
                break
            result.append(q)
            p = q
    
        
        if board[q[0]][q[1]] == 0: #if the line does not end with the current players counter
            result = []
            return result
        elif board[q[0]][q[1]] == a:
            return result
    except IndexError:
        result = []
        return result
        
print(getLine(board, who, pos, dir))     

