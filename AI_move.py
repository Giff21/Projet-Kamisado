# 1)find all the available tiles
# 2)move to a random available tile -> return a list [final_rows, final_column]
# 3)put in common [[initial_rows, initial_column], [final_rows, final_column]]
# 4)find the best move from the available tiles: the closest to the ennemi end without giving the win in the next round -> return a list [final_rows, final_column]
import random
from pawn_finder import find_pawn


def possible_move(dark: list, light: list, pawn: list, player: int) -> list:
    """gives the coordonates of every tiles we can go

    Args:
        dark (list): darks pawn positions
        light (list): light pawns positions
        pawn (list): position of the pawn we havve to play
        player (int): 0 (dark) or 1 (light)

    Returns:
        list: a list of all possible coordonates (list of lists)
    """

    pawn_row = pawn[0]
    pawn_column = pawn[1]
    print(f"position pion:{pawn}")
    towers_positions = dark + light  # updated coo of all towers
    possible_move = []

    # possible movements
    if player == 0:
        directions = [[-1, 0], [-1, 1], [-1, -1]]
    else:
        directions = [[1, 0], [1, -1], [1, 1]]

    # check possible tiles (front, diagonale right then left) and put it in a list
    for dir_rows, dir_column in directions:
        currentRow = pawn_row + dir_rows
        currentColumn = pawn_column + dir_column

        while 0 <= currentRow < 8 and 0 <= currentColumn < 8:  # dimentions of the board
            if [currentRow, currentColumn] in towers_positions:
                break

            possible_move.append([currentRow, currentColumn])
            currentRow += dir_rows
            currentColumn += dir_column

    if not possible_move:
        print("PAS DE MOVE POSSIBLE")
        return [pawn, pawn]

    return possible_move


def minamax() -> list:
    pass


def move(boardState: dict) -> list:
    """take the board information and choose a move with the final position

    Args:
        boardState (dict): current state of the game (color of the tile, pawns and current player)

    Returns:
        list: the tile we want to move from our current position
    """

    dark, light, pawn, player = find_pawn(boardState)
    list_move = possible_move(dark, light, pawn, player)
    final_move = random.choice(list_move)

    print(f"position finale:{final_move}")

    return [pawn, final_move]
