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
    dark, light, Pawn = FindPawn(boardState)
    PawnRow = Pawn[0]
    PawnColumn = Pawn[1]
    print(f'position pion:{Pawn}')
    player = Find_current(boardState)
    tower_position = dark + light #coo of all towers
    #print(tower_position)
    possible_move =[]

    if player == 0:
        directions = [[-1,0], [-1,1], [-1,-1]]
    else:
        directions = [[1,0], [1,-1], [1,1]]

    for Drows, Dcolumn in directions:
        currentRow = PawnRow + Drows
        currentColumn = PawnColumn + Dcolumn

        while 0 <= currentRow < 8 and 0 <= currentColumn < 8:
            if [currentRow, currentColumn] in tower_position:
                break
            
            possible_move.append([currentRow, currentColumn])
            currentRow += Drows
            currentColumn += Dcolumn

    if not possible_move:
        return print("PAS DE MOVE POSSIBLE")

    return random.choice(possible_move)


def Minamax() -> list:
    pass


def move(boardState) -> list:
    
    #Minamax(PossibleMove(boardState))
    return [FindPawn(boardState)[2], PossibleMove(boardState)]


