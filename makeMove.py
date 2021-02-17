# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:05:01 2019

@author: Chloe
"""

board = [[0, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0],
         [2, 2, 2, 2, 2, 1, 1, 1],
         [0, 2, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 2, 1, 2, 0, 0],
         [0, 1, 2, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1, 0, 0]]
move = (7, 4)
who = 2

def makeMove(board, move, who):
    """
    Places a counter on the Othello board and returns the updated board
    
    Parameters
    ----------
    board : An array representing the Othello game board in its current state
            of play
    move : A tuple of the form (r, c) with r and c integers from 0 to 7 which
           corresponds to the row/column index of the position onto which the
           current player will place their disk
    who : An integer, 1 or 2, indicating the current player
    
    Returns
    -------
    board : The updated Othello board after the move has been played and the
            appropriate counters have been changed
            
    Examples
    --------
    >>>board = [[0, 2, 2, 2, 1, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        move = (0, 0)
        who = 1
        This will return
        board = [[1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    >>>board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 2, 2, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        move = (3, 6)
        who = 1
        This will return
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 2, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 1, 2, 1, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    """
    direction = getdir()
    board[move[0]][move[1]] = who #change this space to the current players counter
    for dir in direction:
        line = getLine(board, who, move, dir)
        print(dir, line)
        for j in line:
            if j[0] < 0 or j[1] < 0:
                line = []
        for i in line:
            board[i[0]][i[1]] = who
    return board
    
printBoard(board)
makeMove(board, move, who)
printBoard(board)