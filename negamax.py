from ai_move import possible_move
from pawn_finder import find_pawn
import copy


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


def utility(dark_pos: list, light_pos: list, player: int) -> int:
    """score the number of moves it takes to win

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        player (int): player side 0(dark) 1(light)

    Returns:
        int: winning = +1, losing= -1
    """
    the_winner = winner(dark_pos, light_pos)

    if the_winner is None:
        return 0

    if the_winner == player:
        return 1
    return -1


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
        print("there is a game winner")
        return True  # game over, there is a winner
    if not list_move:
        print("the game is blocked")
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

    # take the info of the old and new tile
    old_cell_color, old_tile = new_board[old_row][
        old_col
    ]  # tile is ["piece_color","pawn_side"]
    new_cell_color, new_tile = new_board[new_row][new_col]
    # erase the pawn in the old position and write it in the new position
    new_board[old_row][old_col] = [old_cell_color, None]
    new_board[new_row][new_col] = [new_cell_color, old_tile]
    # write the new cell_color
    new_state["color"] = new_cell_color
    new_state["current"] = 1 - player

    return new_state


def negamax(
    boardState: dict, list_move: list, alpha=float("-inf"), beta=float("inf")
) -> list:

    dark, light, pawn, player = find_pawn(boardState)
    if game_over(dark, light, list_move):
        return -utility(dark, light, player), None

    the_value, the_move = float("-inf"), None

    for move in list_move:
        # new game positions
        successor = apply(boardState, move, player, pawn)
        new_dark, new_light, new_pawn, new_player = find_pawn(successor)
        new_list_move = possible_move(new_dark, new_light, new_pawn, new_player)
        # iteration
        value, _ = negamax(successor, new_list_move, -beta, -alpha)

        if value > the_value:
            the_value, the_move = value, move
        alpha = max(alpha, the_value)

        if alpha >= beta:
            break
    return the_value, the_move


# circular import probleme
