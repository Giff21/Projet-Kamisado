from src.negamax import winner, heurestic, game_over, apply, negamax, move
from tests.board_test import tboard
from src.pawn_finder import find_pawn
from src.ai_move import possible_move
import copy
import time


def test_winner():
    assert winner([[0, 1]], [[2, 3]]) == 0
    assert winner([[1, 1]], [[7, 3]]) == 1


def test_heuristic():
    dark = [[0, 0]]
    light = [[6, 2]]
    assert heurestic(dark, light, 0, [[1, 1]]) == 9
    assert heurestic(dark, light, 1, [[1, 1]]) == -9
    assert heurestic([[5, 1]], [[2, 2]], 0, [[1, 1]]) == 0
    assert heurestic([[5, 1]], [[2, 2]], 1, [[1, 1]]) == 0
    dark = [[5, 0]]
    light = [[2, 0]]
    val = heurestic(dark, light, 0, [[4, 0]])
    assert isinstance(val, int)


def test_game_over():
    assert game_over([[0, 0]], [[5, 0]], [[1, 0]]) is True
    assert game_over([[3, 0]], [[7, 0]], [[6, 0]]) is True
    assert game_over([[3, 0]], [[4, 0]], []) is True
    assert game_over([[3, 0]], [[4, 0]], [[2, 0]]) is False


def test_apply():
    board = copy.deepcopy(tboard)
    board["board"][5][5] = ["orange", ["blue", "dark"]]
    state = apply(board, [4, 5], 0, [5, 5])
    assert state["board"][5][5][1] is None
    assert state["board"][4][5][1] == ["blue", "dark"]
    assert state["color"] == state["board"][4][5][0]
    assert state["current"] == 1


def test_negamax():
    board = copy.deepcopy(tboard)
    dark, light, pawn, player = find_pawn(board)
    list_move = possible_move(dark, light, pawn, player)
    the_value, the_move = negamax(board, list_move, time.time(), 3, 3)
    assert the_move in list_move
    the_value2, the_move2 = negamax(board, [], time.time(), 3, 3)
    assert the_move2 is None


def test_move():
    board = copy.deepcopy(tboard)
    dark, light, pawn, player = find_pawn(board)
    list_move = possible_move(dark, light, pawn, player)
    result = move(board, strategy=True, time_limit=3)
    assert result[0] == pawn
    assert result[1] in list_move
    result2 = move(board, strategy=False, time_limit=3)
    assert result2[0] == pawn
    assert result2[1] in list_move
