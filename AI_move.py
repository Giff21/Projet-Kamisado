#1)find all the available tiles
#2)move to a random available tile -> return a list [final_rows, final_column]
#3)put in common [[initial_rows, initial_column], [final_rows, final_column]]
#4)find the best move from the available tiles: the closest to the ennemi end without giving the win in the next round -> return a list [final_rows, final_column]

from Pawn_finder import FindPawn

def PossibleMove(boardState):
    pass

def Minamax() -> list:
    pass

def move(boardState) -> list:
    Minamax(PossibleMove(boardState))
    return [FindPawn, Minamax()]