from ai_move import possible_move
from pawn_finder import find_pawn
import copy
import random
import time


def winner(dark_pos: list, light_pos: list) -> int:
    """find the winner player side

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions

    Returns:
        int: the winning player side 0 or 1
    """
    for pos in dark_pos:
        if pos[0] == 0:
            return 0

    for pos in light_pos:
        if pos[0] == 7:
            return 1

    return None


def heurestic(boardState: dict, player: int, list_move: list):
    # we take the move with the lowest distance
    dark_pos, light_pos, pawn, _ = find_pawn(boardState)
    if game_over(dark_pos, light_pos, list_move):
        the_winner = winner(dark_pos, light_pos)
        if the_winner is None:
            return 0
        elif the_winner == player:
            return 9
        return -9

    if player == 0:
        my_distance = min(pos[0] for pos in dark_pos)
        enemy_distance = 7 - max(pos[0] for pos in light_pos)
    else:
        my_distance = 7 - max(pos[0] for pos in light_pos)
        enemy_distance = min(pos[0] for pos in dark_pos)
    return enemy_distance - my_distance


def game_over(dark_pos: list, light_pos: list, list_move: list) -> bool:
    """check if the game has a winner or is blocked

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        list_move (list): all the current moves

    Returns:
        bool: True=game is over, False=game not over
    """

    if winner(dark_pos, light_pos) is not None:
        return True  # game over, there is a winner
    if not list_move:
        return True  # game over, game blocked
    return False


def apply(boardState: dict, move: list, player: int, pawn: list) -> list:
    """create a copy of the current game and play one step further

    Args:
        boardState (dict): the state of the board
        move (list): the move we want to make
        player (int): player side 0(dark) 1(light)
        pawn (list): coo of our pawn

    Returns:
        dict: the new board with the predicted move
    """
    new_state = copy.deepcopy(boardState)  # copy the entire dictionnary
    new_board = new_state["board"]
    new_row, new_col = move
    old_row, old_col = pawn

    # take the info of the old and new tile, tile is ["piece_color","pawn_side"]
    old_cell_color, old_tile = new_board[old_row][old_col]
    new_cell_color, new_tile = new_board[new_row][new_col]

    # erase the pawn in the old position and write it in the new position
    new_board[old_row][old_col] = [old_cell_color, None]
    new_board[new_row][new_col] = [new_cell_color, old_tile]

    # write the new cell_color
    new_state["color"] = new_cell_color
    new_state["current"] = 1 - player

    return new_state


def negamax(
    boardState: dict,
    list_move: list,
    start_time: float,
    time_limit: float,
    depth: int = 4,
    alpha=float("-inf"),
    beta=float("inf"),
) -> list:

    dark, light, pawn, player = find_pawn(boardState)
    if time.time() - start_time > time_limit:
        return -heurestic(boardState, player, list_move), None

    if game_over(dark, light, list_move) or depth == 0:
        return -heurestic(boardState, player, list_move), None

    the_value, the_move = float("-inf"), None

    for move in list_move:
        # new game positions
        successor = apply(boardState, move, player, pawn)
        new_dark, new_light, new_pawn, new_player = find_pawn(successor)
        new_list_move = possible_move(new_dark, new_light, new_pawn, new_player)
        # iteration
        value, _ = negamax(
            successor, new_list_move, start_time, time_limit, depth - 1, -beta, -alpha
        )
        if value > the_value:
            the_value, the_move = value, move
        alpha = max(alpha, the_value)

        if alpha >= beta:
            break
    return -the_value, the_move


def move(boardState: dict, strategy: bool, time_limit: float = 2.5) -> list:
    """take the board information and choose a move with the final position

    Args:
        boardState (dict): current state of the game (color of the tile, pawns and current player)

    Returns:
        list: the tile we want to move from our current position
    """
    dark, light, pawn, player = find_pawn(boardState)
    list_move = possible_move(dark, light, pawn, player)

    if strategy:
        # print("SMART MOVE")
        start_time = time.time()
        for depth in range(1, 20):
            if time.time() - start_time > time_limit:
                break
            _, final_move = negamax(
                boardState,
                list_move,
                start_time,
                time_limit,
                depth,
                alpha=float("-inf"),
                beta=float("inf"),
            )
        print(f"depth: {depth}, best move: {final_move} ")
    else:
        final_move = random.choice(list_move)
        # print("STUPID MOVE")

    print(f"starting position:{pawn}")

    return [pawn, final_move]
