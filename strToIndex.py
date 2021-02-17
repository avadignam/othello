# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:13:10 2019

@author: Chloe
"""

def strToIndex(s):
    """
    Parameters
    ----------
    s : A string indicating a place on the game board that must be converted to
        to an index that can be used in the Python coding
        
    Returns
    -------
    (k, j) : A tuple pertaining to the specified place on the game board
    
    Raises
    ------
    ValueError : If the string entered does not correspond to a place on the board
                 Prints the message "Invalid Argument. Try another go!"
    
    Examples
    --------
    These should return (3, 2)
    >>> strToIndex("C4")
    >>> strToIndex("4c")
    >>> strToIndex("   c 4 ")
    These should raise ValueError and the appropriate message
    >>> strToIndex("   x 9 ")
    >>> strToIndex("c3 3 ")
    """
    t = s.replace(" ", "")
    for m in s:
        if m.isdigit():
            t = t.replace(m, "")
        
    for i in t:
        if i.lower() == "a":
            j = 0
            break
        elif i.lower() == "b":
            j = 1
            break
        elif i.lower() == "c":
            j = 2
            break
        elif i.lower() == "d":
            j = 3
            break
        elif i.lower() == "e":
            j = 4
            break
        elif i.lower() == "f":
            j = 5
            break
        elif i.lower() == "g":
            j = 6
            break
        elif i.lower() == "h":
            j = 7
            break
        else:
            raise ValueError("Invalid argument. Try another go!")
    n = int(''.join(x for x in s if x.isdigit()))
    if n <= 8:
        k = n-1
    else:
        raise ValueError("Invalid argument. Try another go!")
        
    
    return ((k, j))
    
print(strToIndex("  4 c "))