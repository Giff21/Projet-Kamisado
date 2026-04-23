#1)find all the available tiles
#2)move to a random available tile -> return a list [final_rows, final_column]
#3)put in common [[initial_rows, initial_column], [final_rows, final_column]]
#4)find the best move from the available tiles: the closest to the ennemi end without giving the win in the next round -> return a list [final_rows, final_column]
import random
from Pawn_finder import FindPawn
from Pawn_finder import Find_current





def PossibleMove(boardState):
    """Return [finale raw, final column]

    descr : tell a direction to this function and will give you all tha available move
    
    """
    currentRow = FindPawn(boardState)[2][0]
    currentColumn = FindPawn(boardState)[2][1]
    direction = random.choice(["forward", "Rdiagonal", "Ldiagonal"])

    tower_position = FindPawn(boardState)[0] + FindPawn(boardState)[1]


    if Find_current(boardState) == 0:
        if direction == 'forward':
            finalPosition = [currentRow-1, currentColumn]
        if direction == 'Rdiagonal':
            finalPosition = [currentRow-1, currentColumn+1]
        if direction == 'Ldiagonal':
            finalPosition = [currentRow-1, currentColumn-1]

    elif Find_current(boardState) == 1:
        if direction == 'forward':
            finalPosition = [currentRow+1, currentColumn]
        if direction == 'Rdiagonal':
            finalPosition = [currentRow+1, currentColumn-1]
        if direction == 'Ldiagonal':
            finalPosition = [currentRow+1, currentColumn+1]

    return finalPosition

def Minamax() -> list:
    pass

def move(boardState) -> list:
    
    #Minamax(PossibleMove(boardState))
    return [FindPawn(boardState)[2], PossibleMove(boardState)]


