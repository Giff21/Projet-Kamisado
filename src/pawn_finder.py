import random


def find_pawn(boardState: dict) -> tuple:
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
    chosen_pos = None  # first we don't know the position of our pawn

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
