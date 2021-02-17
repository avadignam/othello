# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:01:50 2019

@author: Chloe
"""
from copy import deepcopy

board = [[2, 2, 2, 2, 2, 0, 0, 0],
         [2, 2, 1, 2, 2, 2, 0, 0],
         [2, 1, 2, 1, 2, 2, 0, 0],
         [2, 1, 1, 2, 1, 0, 0, 0],
         [2, 1, 2, 0, 0, 0, 0, 1],
         [0, 2, 2, 1, 2, 1, 1, 0],
         [0, 0, 2, 1, 1, 0, 0, 0],
         [0, 2, 1, 2, 1, 0, 0, 0]]

who = 1

def suggestMove1(board, who):
    """
    Calculates the highest score a player could achieve from the valid moves
    
    Parameters
    ----------
    board : An array representing the Othello game board in its current state
            of play
    who : An integer, 1 or 2, indicating which players turn it is
    
    Returns
    -------
    turn : A tuple of the format (r, c) with r and c integers from 0 to 7
           corresponding to the row/column index of the suggested position for
           player who to place a disk on
           
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
        This will return the tuple (3, 6) as this is the only move that leads
        to a score of 7, the largest achievable for player 1 from this 
        configuration
    
    >>>board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 1, 2, 2, 2, 0, 0],
                [0, 0, 1, 2, 1, 0, 0, 0],
                [0, 0, 0, 2, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        who = 2
        For player 2, this configuration has the following possible moves:
            [(2, 1), (3, 1), (4, 1), (5, 5), (6, 4)]
        as they all lead to a score of -5, the best achievable (most negative)
        for player 2 from this configuration.
        The function should return (2, 1) as it is the first in the list and 
        will only overwrite the score if the new score is larger than the
        previous one
        
    """
    valid = getValidMoves(board, who)
    board2 = deepcopy(board)
    score = scoreBoard(board2)
    count = 0
    for m in valid:
        board2 = makeMove(board2, m, who)
        newscore = scoreBoard(board2)
        print(m, newscore)
        if who == 1:
            if newscore > score:
                score = newscore
                turn = m
        elif who == 2:
            if newscore < score:
                score = newscore
                turn = m
        board2 = deepcopy(board)
            
    return turn

print(suggestMove1(board, who))