# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:40:18 2019

@author: Chloe
"""

def indexToStr(t):
    """
    Parameters
    ----------
    t : A tuple of the form (i, j) with 0 <= i, j <= 7 that corresponds to a 
        place on the game board
    
    Returns
    -------
    A string which corresponds to a place on the game board that the player can
    easily comprehend
    
    Examples
    --------
    (3, 2) should return c4
    
    """
    if t[1] == 0:
        i = "a"
    elif t[1] == 1:
        i = "b"
    elif t[1] == 2:
        i = "c"
    elif t[1] == 3:
        i = "d"
    elif t[1] == 4:
        i = "e"
    elif t[1] == 5:
        i = "f"
    elif t[1] == 6:
        i = "g"
    elif t[1] == 7:
        i = "h"
        
    for n in range(8):
        if t[0] == n:
            j = n+1
    return "{}{}".format(i, j)

t = (7, 4)
print(indexToStr(t))