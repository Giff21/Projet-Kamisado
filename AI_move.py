#1)find all the available tiles
#2)move to a random available tile -> return a list [final_rows, final_column]
#3)put in common [[initial_rows, initial_column], [final_rows, final_column]]
#4)find the best move from the available tiles: the closest to the ennemi end without giving the win in the next round -> return a list [final_rows, final_column]
import random
from Pawn_finder2 import FindPawn2


def PossibleMove(dark, light, pawn, player):
    """Return [finale raw, final column]
    args :  dark : list of dark pawn positions
            light : list of light pawn positions
            pawn : position of the pawn we need to move
            player : we are 0 (dark) or 1 (light)

    descr : tell a direction to this function and will give you all tha available move
    
    """

    PawnRow = pawn[0]
    PawnColumn = pawn[1]
    print(f'position pion:{pawn}')
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
        print("PAS DE MOVE POSSIBLE")
        return [pawn, pawn]

    return possible_move


def Minamax() -> list:
    pass


def move(boardState) -> list:
    """Return [[initRow, initCol],[finalRow, finalCOl]]

    descr : take the board inforamtion from FindPawn2 give it to possibleMove that find a final pawn tile
    
    """
    dark, light, pawn, player = FindPawn2(boardState)
    list_move = PossibleMove(dark, light, pawn, player)
    final_move = random.choice(list_move)

    print(f'position finale:{final_move}')

    return [pawn, final_move]


