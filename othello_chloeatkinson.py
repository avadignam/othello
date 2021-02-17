# -*- coding: utf-8 -*-
"""
A Python module for the Othello game.

Othello is a 2 player game played on an 8x8 board. There are 64 counters with
a light and dark side. The players take turns to place their counters on the 
board with their colour facing up. When a player places a counter such that a
line (vertical, horizontal or diagonal) of the other players counters is 
between two counters of their own colour, the other players counters caught
between are flipped.

Full name: Chloe Atkinson
StudentId: 9858617
Email: chloe.atkinson-2@student.manchester.ac.uk
"""

from copy import deepcopy

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
                       [0, 0, 0, 2, 1, 0, 0, 0],
                       [0, 0, 0, 1, 2, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
            }
    
    return game

def printBoard(board):
    """
    Prints a game board of the correct format for playing Othello, with values
    along the top and left hand side to clearly indicate the spaces
    
    Parameters
    ----------
    board : an array (list of lists) of 8 lists with 8 elements, with values 
            either 0, 1 or 2
            
    Prints
    ------
    An uncheckered game board suitable for playing Othello 
    
    Example
    -------
    bo5ard = [[0, 0, 0, 0, 0, 0, 0, 0],
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
    
def strToIndex(s):
    """
    Takes a string s as argument and returns a tuple (r, c) with r and c 
    corresponding to the indices of the associated row and column position
    
    Parameters
    ----------
    s : A string indicating a place on the game board that must be converted to
        to an index that can be used in the Python coding
        
    Returns
    -------
    (r, c) : A tuple pertaining to the specified place on the game board
    
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
    t = s.replace(" ", "") # Ensures the input is of the correct form
    for m in s:
        if m.isdigit(): 
            t = t.replace(m, "") # Ensures the input is of the correct form
        
    for i in t:
        if i.lower() == "a":
            c = 0
            break
        elif i.lower() == "b":
            c = 1
            break
        elif i.lower() == "c":
            c = 2
            break
        elif i.lower() == "d":
            c = 3
            break
        elif i.lower() == "e":
            c = 4
            break
        elif i.lower() == "f":
            c = 5
            break
        elif i.lower() == "g":
            c = 6
            break
        elif i.lower() == "h":
            c = 7
            break
        else:
            raise ValueError("Invalid argument. Try another go!")
    n = int(''.join(x for x in s if x.isdigit()))
    if n <= 8:
        r = n-1
    else:
        raise ValueError("Invalid argument. Try another go!")
        
    
    return ((r, c))

def indexToStr(t):
    """
    Takes as argument a tuple t of the form (r, c) with r and c corresponding
    to the indices of the associated board row/column position and returns a 
    2-character string corresponding to the board column/row position
    
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
    
    f.pop(0) function learned from https://docs.python.org/2/tutorial/datastructures.html
    """

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
    if who == 1: #Condenses the code as no need to write out the same thing twice
        a = 1
        b = 2
    elif who == 2:
        a = 2
        b = 1
        
    try:
        while board[q[0]][q[1]] == b: #while the counters belong to the other person
            q = (p[0]+dir[0], p[1]+dir[1])
            if board[q[0]][q[1]] != b: #if the next space is not occupied by the other persons counter
                break
            result.append(q) #add this space to the list
            p = q
            
        if board[q[0]][q[1]] == 0: #if the line does not end with the current players counter
            result = []
            return result
        elif board[q[0]][q[1]] == a: #if the line ends with the current players counter
            return result
    except IndexError:
        result = []
        return result
    
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
    position = getTile(board) #a list of all possible spaces on the board
    direction = getdir() #a list of all possible directions on the board
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
            if board[row][col] == 0: #only adds empty spaces
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
    board[move[0]][move[1]] = who #place a counter on the empty space
    for dir in direction:
        line = getLine(board, who, move, dir)
        for j in line:
            if j[0] < 0 or j[1] < 0:
                line = []
        for i in line:
            board[i[0]][i[1]] = who # flip all the counters along the line 
    return board

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
            if j == 1: # if the space is occupied by player1's counter
                x += 1
            elif j == 2: # if the space is occupied by player2's counter
                y -= 1
    
    return x + y

def suggestMove(board, who):
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
    board2 = deepcopy(board) # so as to not affect the current board
    score = scoreBoard(board2)
    for m in valid:
        board2 = makeMove(board2, m, who) #test out all possible moves
        newscore = scoreBoard(board2)
        if who == 1:
            if newscore > score:
                score = newscore
                turn = m
        elif who == 2:
            if newscore < score:
                score = newscore
                turn = m
        board2 = deepcopy(board) #reset the dummy board to a copy of the actual board
            
    return turn


# ------------------- Main function --------------------
def play():
    """
    Triggers the gameplay of Othello, either a new game or loaded from a file
    game.txt, until there are no valid moves left for either player, at which
    point an appropriate message is printed and the winner is announced.
    
    Raises
    ------
    FileNotFoundError : If asked to load a saved game that is not in the same
                        file
    """
    print("*"*56)
    print("***"+" "*9+"WELCOME TO CHLOE'S OTHELLO GAME!"+" "*9+"***")
    print("*"*56,"\n")
    print("Enter the players' names, or type 'C' for computer or 'L' to load a saved game.\n")
    player1 = input("Enter player 1: ").capitalize()
    while player1 == "": #if no input given, repeat
        player1 = input("Enter player 1: ").capitalize()
        
    if player1 == "L":
        game = loadGame()
        print("\nLoading previous game ... ")
        player1 = game.get('player1', 'None').capitalize() #set parameters to names to dictionary keys
        player2 = game.get('player2', 'None').capitalize()
        
        print("\nPlayer 1: {}".format(player1))
        print("\nPlayer 2: {}".format(player2))
    else:
        player2 = input("Enter player 2: ").capitalize()
        while player2 == "":
            player2 = input("Enter player 2: ").capitalize()
        game = newGame(player1, player2)
        
    who = game.get('who', 'None')
    board = game.get('board', 'None')   
    
    print("\nLet's play!\n")
    
    printBoard(board)
    
    def player1go(board, who):
        """
        Takes player1's move and resets the board as it would look after the move
        has been made
    
        Parameters
        ----------
        board : An array representing the Othello game board in its current state
                of play
                who : An integer, 1 or 2, indicating which players turn it is
        """
        if player1 == "C": # if player1 is computer
            if getValidMoves(board, 2)==[] and getValidMoves(board, 1) != []:
                move = suggestMove(board, who)
                print("\nComputer (X) is thinking... and chose to move {}.".format(indexToStr(move)))
                makeMove(board, move, who) # make the suggested move
                print("")
                printBoard(board)
                who = 2
                player2go(board, who)
            elif getValidMoves(board, 1) != []: #only if there are still valid moves
                move = suggestMove(board, who)
                print("\nComputer (X) is thinking... and chose to move {}.".format(indexToStr(move)))
                makeMove(board, move, who) # make the suggested move
                print("")
                printBoard(board)
                who = 2
                player2go(board, who)
            elif getValidMoves(board, 1) == [] and getValidMoves(board, 2) != []:
                print("No valid moves for current player. Skipping turn...")
                who = 2
                player2go(board, who)
            elif getValidMoves(board, 1) == [] and getValidMoves(board, 2) == 2:
                endgame(board, player1, player2)
        else:
            if getValidMoves(board, 2)==[] and getValidMoves(board, 1) != []:
                while True:
                    try:
                        s = input("{} (X): Where will your counter go? ".format(player1))
                        move = strToIndex(s) #take the input as something the functions can read
                        if move not in getValidMoves(board, who): #if its not a valid move
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid argument. Try another go!")
                makeMove(board, move, who)
                print("")
                printBoard(board)
                
                player2go(board, who)
            elif getValidMoves(board, 1) != []: #only if there are still valid moves
                while True:
                    try:
                        s = input("{} (X): Where will your counter go? ".format(player1))
                        move = strToIndex(s) #take the input as something the functions can read
                        if move not in getValidMoves(board, who): #if its not a valid move
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid argument. Try another go!")
                makeMove(board, move, who)
                print("")
                printBoard(board)
                who = 2
                player2go(board, who)
            elif getValidMoves(board, 1) == [] and getValidMoves(board, 2) != []:
                print("No valid moves for current player. Skipping turn...")
                who = 2
                player2go(board, who)
            elif getValidMoves(board, 1) == [] and getValidMoves(board, 2) == 2:
                endgame(board, player1, player2)
        
    
    def player2go(board, who):
        """
        Takes player2's move and resets the board as it would look after the move
        has been made
        
        Parameters
        ----------
        board : An array representing the Othello game board in its current state
                of play
                who : An integer, 1 or 2, indicating which players turn it is
                
        """
        if player2 == "C": # if player2 is computer
            if getValidMoves(board, 1)==[] and getValidMoves(board, 2) != []:
                move = suggestMove(board, who)
                print("\nComputer (O) is thinking... and chose to move {}.".format(indexToStr(move)))
                makeMove(board, move, who)
                print("")
                printBoard(board)
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 2) != []: # only if there are still valid moves
                move = suggestMove(board, who)
                print("\nComputer (O) is thinking... and chose to move {}.".format(indexToStr(move)))
                makeMove(board, move, who)
                print("")
                printBoard(board)
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 2) == [] and getValidMoves(board, 1) != []:
                print("No valid moves for current player. Skipping turn...")
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 1)==[] and getValidMoves(board, 2) == []:
                endgame(board, player1, player2)
                
        else:
            if getValidMoves(board, 1)==[] and getValidMoves(board, 2) != []:
                while True:
                    try:
                        s = input("{} (O): Where will your counter go? ".format(player2))
                        move = strToIndex(s) # take the input as something the functions can read
                        if move not in getValidMoves(board, who): # if its not a valid move
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid argument. Try another go!")
                makeMove(board, move, who)
                print("")
                printBoard(board)
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 2) != []: #only if there are still valid moves
                while True:
                    try:
                        s = input("{} (O): Where will your counter go? ".format(player2))
                        move = strToIndex(s) # take the input as something the functions can read
                        if move not in getValidMoves(board, who): # if its not a valid move
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid argument. Try another go!")
                makeMove(board, move, who)
                print("")
                printBoard(board)
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 2) == [] and getValidMoves(board, 1) != []:
                print("No valid moves for current player. Skipping turn...")
                who = 1
                player1go(board, who)
            elif getValidMoves(board, 1)==[] and getValidMoves(board, 2) == []:
                endgame(board, player1, player2)
        
                
    def endgame(board, player1, player2):
        """
        Prints the appropriate message for who has won the game
    
        Parameters
        ----------
        board : An array representing the Othello game board in its current state
                of play
        player1 : a string indicating who the first player is, is equal to 'C' if 
                  this player is a computer
        player2 : same as above
    
        """
        print("\nGame Over! No more valid moves for each player.")
        if scoreBoard(board) > 0:
            print("{} (X) wins with a score of {}!".format(player1, scoreBoard(board)))
        elif scoreBoard(board) < 0:
            print("{} (O) wins with a score of {}!".format(player2, abs(scoreBoard(board))))
        
    if who == 1:  
        player1go(board, who)
    elif who == 2:
        player2go(board, who)
    
    
if __name__ == '__main__' or __name__ == 'builtins':
    play()