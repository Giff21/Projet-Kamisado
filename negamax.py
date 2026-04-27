from ai_move import possible_move


def winner(dark_pos: list, light_pos: list) -> int:
    """find the winner player side

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        player (int): player side 0(dark) 1(light)

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


def game_over(dark_pos: list, light_pos: list) -> bool:
    """check if the game has a winner or is blocked

    Args:
        dark_pos (list): dark pawns positions
        light_pos (list): light panws positions
        player (int): player side 0(dark) 1(light)

    Returns:
        bool: True=game is over, False=game not over
    """
    if winner(dark_pos, light_pos) is not None:
        print("there is a game winner")
        return True  # game over, there is a winner
    if len(possible_move) == 0:
        print("the game is blocked")
        return True  # game over, game blocked
    return False
