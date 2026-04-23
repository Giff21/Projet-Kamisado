#1)find all the available tiles
#2)move to a random available tile -> return a list [final_rows, final_column]
#3)put in common [[initial_rows, initial_column], [final_rows, final_column]]
#4)find the best move from the available tiles: the closest to the ennemi end without giving the win in the next round -> return a list [final_rows, final_column]
import random
from Pawn_finder import FindPawn
from Pawn_finder import Find_current

def rules():
    tower_position = [] #list with position af all tawer -> do not go
    pass



def PossibleMove(boardState, direction):
    """Return [finale raw, final column]

    descr : tell a direction to this function and will give you all tha available move
    
    """
    currentRow = FindPawn(boardState)[0]
    currentColumn = FindPawn(boardState)[1]

    if Find_current(boardState) == 0:
        if direction == 'forward':
            finalPosition = [currentRow-random.randint(0,currentRow), currentColumn]
        if direction == 'Rdiagonal':
            finalPosition = [currentRow-random.randint(0,currentRow), currentColumn+random.randint(0,currentColumn)]
        if direction == 'Ldiagonal':
            finalPosition = [currentRow-random.randint(0,currentRow), currentColumn-random.randint(0,currentColumn)]

    elif Find_current(boardState) == 1:
        if direction == 'forward':
            finalPosition = [currentRow+random.randint(0,7-currentRow), currentColumn]
        if direction == 'Rdiagonal':
            finalPosition = [currentRow+random.randint(0,7-currentRow), currentColumn-random.randint(0,7-currentColumn)]
        if direction == 'Ldiagonal':
            finalPosition = [currentRow+random.randint(0,7-currentRow), currentColumn+random.randint(0,7-currentColumn)]

    return finalPosition

def Minamax() -> list:
    pass

def move(boardState) -> list:
    direction = random.choice(["forward", "Rdiagonal", "Ldiagonal"])
    Minamax(PossibleMove(boardState))
    return [FindPawn, PossibleMove(boardState, direction)]