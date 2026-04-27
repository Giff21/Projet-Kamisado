# JF, you can put your stuff here in order to find the tile to play
# 1)find the position of all the pawn, light or dark and if we are dark(0) or light(1)
# 2)the fonction must return a list of the pawn we want to play [initial_rows, initial_column] first and then the pawn we must play according
# to the color the enemy ended
# 3)later give me the color of the ennemis to pervent Flo to tell our pawn to go on the color that will get the will to the ennemi

import random


def find_pawn(boardState: dict) -> list:
    """goes through the board and find all the pawns informations

    Args:
        boardState (dict): current state of the game

    Returns:
        list: position of the dark pawns, light pawns, our pawn, player side
    """
    board_state = boardState["board"]
    pawn_color = boardState["color"]
    current_side = boardState["current"]

    dark_pawn = []
    light_pawn = []
    chosen_pos = None  # coo of our pawn, at first there is no forced tile to move

    if current_side == 0:
        pawn_team = "dark"
    else:
        pawn_team = "light"

    # goes through the board and save coo of all pawns in lists
    for row in range(8):
        for col in range(8):
            cell_color, tile = board_state[row][col]
            if isinstance(tile, list):
                piece_color, pawn_side = tile
                if pawn_side == "dark":
                    dark_pawn.append([row, col])
                else:
                    light_pawn.append([row, col])
                if pawn_color == piece_color and pawn_team == pawn_side:
                    chosen_pos = [row, col]
    # for the first pawn
    if pawn_color is None:
        candidates = dark_pawn
        chosen_pos = random.choice(candidates)

    return dark_pawn, light_pawn, chosen_pos, current_side
