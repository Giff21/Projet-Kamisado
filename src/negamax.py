from src.ai_move import possible_move
from src.pawn_finder import find_pawn
import random
import time
import copy


def winner(dark_pos: list, light_pos: list) -> int:
    """find the winner player side

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions

    Returns:
        int: the winning player side 0(dark) or 1(light)
    """
    for pos in dark_pos:
        if pos[0] == 0:  # dark win in row 0
            return 0

    for pos in light_pos:
        if pos[0] == 7:  # light win in row 7
            return 1

    return None


def heurestic(dark_pos: list, light_pos: list, player: int, list_move: list) -> int:
    """score to find the shortest distance from the winning positions

    Args:
        dark_pos (list): positions of all dark pawns
        light_pos (list): positions of all light pawns
        player (int): current side 0(dark) 1(light)
        list_move (list): all available move from the pawn tile

    Returns:
        int: score
    """
    if game_over(dark_pos, light_pos, list_move):
        the_winner = winner(dark_pos, light_pos)
        if the_winner is None:
            return 0
        elif the_winner == player:
            return 9  # victory is +9 points
        return -9

    dark_rows = [pos[0] for pos in dark_pos]
    light_rows = [pos[0] for pos in light_pos]
    if player == 0:
        my_distance = min(dark_rows)
        enemy_distance = 7 - max(light_rows)
    else:
        my_distance = 7 - max(light_rows)
        enemy_distance = min(dark_rows)

    return enemy_distance - my_distance  # positive I'm closest to winning, negative ennemy is closest to winning


def game_over(dark_pos: list, light_pos: list, list_move: list) -> bool:
    """check if the game has a winner or is blocked

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        list_move (list): all available move from the pawn tile

    Returns:
        bool: True=game is over, False=game not over
    """
    if winner(dark_pos, light_pos) is not None:
        return True

    if not list_move:
        return True

    return False


def apply(boardState: dict, move: list, player: int, pawn: list) -> dict:
    """create a copy of the current game and play one step further

    Args:
        boardState (dict): the state of the board
        move (list): the move we want to make
        player (int): player side 0(dark) 1(light)
        pawn (list): coo of our pawn

    Returns:
        dict: the new board with the predicted move
    """
    # copy the entire dictionnary
    new_state = copy.deepcopy(boardState)
    new_board = new_state["board"]
    new_row, new_col = move
    old_row, old_col = pawn

    # take the info of the two tiles that will be modified
    old_cellcolor, old_tile = new_board[old_row][old_col]
    new_cellcolor, new_tile = new_board[new_row][new_col]

    # erase and write new positions
    new_board[old_row][old_col] = [old_cellcolor, None]
    new_board[new_row][new_col] = [new_cellcolor, old_tile]
    new_state["color"] = new_cellcolor
    new_state["current"] = 1 - player

    return new_state


def negamax(
    boardState: dict,
    list_move: list,
    start_time: float,
    time_limit: float,
    depth: int,
    alpha=float("-inf"),
    beta=float("inf"),
) -> list:
    """find the mest final coordonates by choosing the best move (highest score)

    Args:
        boardState (dict): state of the game
        list_move (list): all the available moves
        start_time (float): start of the timer
        time_limit (float): maximum time a play can last (max 3s)
        depth (int): how much further play we make
        alpha (float, optional): current highest value. Defaults to float("-inf").
        beta (float, optional): current smallest value. Defaults to float("inf").

    Returns:
        list: best move score, best final coordanate
    """
    dark, light, pawn, player = find_pawn(boardState)

    if (time.time() - start_time > time_limit) or game_over(dark, light, list_move) or depth == 0:
        return -heurestic(dark, light, player, list_move), None

    the_value, the_move = float("-inf"), None

    for move in list_move:
        # find the pawn and moves available of a simulated game
        successor = apply(boardState, move, player, pawn)
        new_dark, new_light, new_pawn, new_player = find_pawn(successor)
        new_list_move = possible_move(new_dark, new_light, new_pawn, new_player)
        value, _ = negamax(successor, new_list_move, start_time, time_limit, depth - 1, -beta, -alpha)  # iteration

        # find the best move (closest ot 0 value)
        if value > the_value:
            the_value, the_move = value, move
        alpha = max(alpha, the_value)

        if alpha >= beta:
            break  # cut the unnecessary  branchs
    return -the_value, the_move


def move(boardState: dict, strategy: bool, time_limit: float = 2.5) -> list:
    """choose the final position

    Args:
        boardState (dict): state of the game
        strategy (bool): algorithm (True) or random (False)
        time_limit (float, optional): must send after this limit. Defaults to 2.5.

    Returns:
        list: pawn tile and final tile coordonates
    """

    dark, light, pawn, player = find_pawn(boardState)
    list_move = possible_move(dark, light, pawn, player)
    best_move_saved = []

    if strategy:
        start_time = time.time()
        for depth in range(1, 20):  # 20 is arbitrary (usually around depth 8-12)
            if time.time() - start_time > time_limit:
                break
            _, candidate = negamax(
                boardState,
                list_move,
                start_time,
                time_limit,
                depth,
                alpha=float("-inf"),
                beta=float("inf"),
            )
            if candidate is not None:
                best_move_saved = candidate  # keep completed depths
        final_move = best_move_saved

        print(f"depth: {depth}, best move: {final_move} ")
    else:
        final_move = random.choice(list_move)

    print(f"starting position:{pawn}")

    return [pawn, final_move]
