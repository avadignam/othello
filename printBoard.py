# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:17:54 2019

@author: Chloe
"""

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

def printBoard(board):
    """
    Parameters
    ----------
    board : an array (list of lists) of 8 lists with 8 elements, with values either
            0, 1 or 2
            
    Prints
    ------
    An uncheckered game board suitable for playing Othello 
    
    Example
    -------
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 2, 0, 0, 0],
             [0, 0, 0, 2, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    
    """
    r = 1 #Row number to begin
    
    header = " |" + "|".join(["a", "b", "c", "d", "e", "f", "g", "h"]) + "|" + "\n" + \
    " " + "-".join("+" for _ in range(9)) #Creates an appealling header for the board
    
    print(header)
    
    for row in board:
        rows = str(row)
        row2 = "{}".format(r) + "|" #Numbers the rows and separates from the board
        for i in rows: # Replacing the values with appealing characters
            if i == "0": 
                j = " " 
                row2 += j + "|"
                
            elif i == "1":
                j = "X"
                row2 += j + "|"
                
            elif i == "2":
                j = "O"
                row2 += j + "|"
        r += 1 # The next row will be one more
        print(row2)
    end = " " + "-".join("+" for _ in range(9))
    print(end)        

printBoard(board)

