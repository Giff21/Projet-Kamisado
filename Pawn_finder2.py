# JF, you can put your stuff here in order to find the tile to play
#1)find the position of all the pawn, light or dark and if we are dark(0) or light(1)
#2)the fonction must return a list of the pawn we want to play [initial_rows, initial_column] first and then the pawn we must play according 
# to the color the enemy ended
#3)later give me the color of the ennemis to pervent Flo to tell our pawn to go on the color that will get the will to the ennemi

import random

def FindPawn2(boardState) -> list:
    iniState = boardState['board']
    headColor = boardState['color']
    current = boardState["current"]

    darkPawn = []
    lightPawn = []
    chosen_pos = None

    if current == 0:
        Pawncolor = 'dark'
    else:
        Pawncolor = 'light'

    for i in range(8):
        for j in range(8):
            cell_color, tile = iniState[i][j]
            if isinstance(tile, list):
                piece_color, pawn_side = tile
                if pawn_side == 'dark':
                    darkPawn.append([i,j])
                else:
                    lightPawn.append([i,j])
                if headColor == piece_color and Pawncolor == pawn_side :
                    chosen_pos = [i, j]
    #for the first pawn
    if headColor is None:
        candidates = darkPawn 
        chosen_pos = random.choice(candidates)

    return darkPawn, lightPawn, chosen_pos, current