from ai_move import possible_move
from pawn_finder import find_pawn
import random
import time


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
    """find the shortest distance from the winning positions

    Args:
        dark_pos (list): positions of all dark pawns
        light_pos (list): positions of all light pawns
        player (int): current side 0(dark) 1(light)
        list_move (list): all available move from the pawn tile

    Returns:
        int: positive I'm closest to winning, negative ennemy is closest to winning
    """
    if game_over(dark_pos, light_pos, list_move):
        the_winner = winner(dark_pos, light_pos)
        if the_winner is None:
            return 0
        elif the_winner == player:
            return 9  # victory is +9 points
        return -9

    # calculate the distance from winning
    dark_rows = [pos[0] for pos in dark_pos]
    light_rows = [pos[0] for pos in light_pos]
    if player == 0:
        my_distance = min(dark_rows)
        enemy_distance = 7 - max(light_rows)
    else:
        my_distance = 7 - max(light_rows)
        enemy_distance = min(dark_rows)

    return enemy_distance - my_distance


def game_over(dark_pos: list, light_pos: list, list_move: list) -> bool:
    """check if the game is over: has a winner or is blocked

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        list_move (list): all the current moves

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
    new_state = {
        "board": [row[:] for row in boardState["board"]],
        "color": boardState["color"],
        "current": boardState["current"],
    }
    new_board = new_state["board"]
    new_row, new_col = move
    old_row, old_col = pawn

    # take the info of the starting tile and the final tile, tile is ["piece_color","pawn_side"]
    old_cell_color, old_tile = new_board[old_row][old_col]
    new_cell_color, new_tile = new_board[new_row][new_col]

    # erase the pawn in the old position and write it in the new position
    new_board[old_row][old_col] = [old_cell_color, None]
    new_board[new_row][new_col] = [new_cell_color, old_tile]

    # write the new cell_color and change plyer turn
    new_state["color"] = new_cell_color
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
        depth (int): how much further play we want to make
        alpha (float, optional): current highest value. Defaults to float("-inf").
        beta (float, optional): current smallest value. Defaults to float("inf").

    Returns:
        list: best move score, best final coordanate
    """
    dark, light, pawn, player = find_pawn(boardState)

    # if longer than time_limit, we play the best move found in the depth, same thing with game over or no play possible
    if (
        (time.time() - start_time > time_limit)
        or game_over(dark, light, list_move)
        or depth == 0
    ):
        return -heurestic(dark, light, player, list_move), None

    the_value, the_move = float("-inf"), None  # best score initialize

    for move in list_move:
        # find the pawn and moves available of a similated game
        successor = apply(boardState, move, player, pawn)
        new_dark, new_light, new_pawn, new_player = find_pawn(successor)
        new_list_move = possible_move(new_dark, new_light, new_pawn, new_player)
        # iteration, we now take the place of the opponent
        value, _ = negamax(
            successor, new_list_move, start_time, time_limit, depth - 1, -beta, -alpha
        )
        # find the best move (closest ot 0 value)
        if value > the_value:
            the_value, the_move = value, move
        alpha = max(alpha, the_value)

        if alpha >= beta:
            break  # cut the unessesary branchs
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
    best_move_saved = []

    if strategy:
        # print("SMART MOVE")
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
        # print("STUPID MOVE")

    print(f"starting position:{pawn}")

    return [pawn, final_move]
