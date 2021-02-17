# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:55:17 2019

@author: Chloe
"""

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 2, 1, 0, 0, 0],
         [0, 0, 1, 2, 2, 2, 0, 0],
         [0, 0, 1, 2, 1, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
who = 2


def getValidMoves(board, who):
    """
    Creates a list of tuples indicating possible moves for a player to make in
    the game Othello
    
    Parameters
    ----------
    board : An array that represents the Othello board as it looks in the 
            current state of play
    who : An integer, 1 or 2, indicating which player is currently playing
    
    Returns
    -------
    result : A list of tupples of the format (r, c), where r and c are integers
             from 0 to 7 corresponding to the indices of the board rows/columns
             of possible moves a player can perform
             If there are no valid moves, the function will return an empty list
    
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
        This should return [(1, 4), (2, 6), (3, 6), (4, 6), (5, 2), (6, 2),
                            (6, 4)]
    >>>board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 2, 2, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        who = 2
        This should return [(1, 1), (1, 3), (1, 4), (1, 5), (2, 1), (2, 5),
                            (3, 1), (4, 1), (4, 5), (5, 1), (5, 5), (6, 4),
                            (6, 5)]
    
    """
    result = []
    position = getTile(board)
    direction = getdir()
    for pos in position:
        for dir in direction:
            p = getLine(board, who, pos, dir)
            if p != []:
                if pos not in result:
                    result.append(pos)
    
    return result

def getTile(board):
    """
    Iterates over every element in every list in board to create a list of
    tuples of the format (r, c), where r and c are integers from 0 to 7
    corresponding to the indices of the board rows/columns for every place in
    board that is not occupied by another players counters
    
    Parameters
    ----------
    board : The Othello board in its current state of play
    
    Returns
    -------
    position : A list of tuples corresponding to every empty place on the
               Othello board
    """
    position = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                position.append((row, col))
    return position

def getdir():
    """
    Creates a list of tuples of the format (r, c) with r and c integers -1, 0,
    or 1, corresponding to directions on the Othello board
    
    Returns
    -------
    direction : a list of tuples corresponding to the directions on the Othello
                board
                [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1),
                (1, 0), (1, 1)]
    """
    direction = []
    for row in range(-1, 2):
        for col in range(-1, 2):
            direction.append((row, col))
    return direction

print(getdir())