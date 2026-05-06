from src.negamax import winner, heurestic, game_over, apply
from tests.board_test import tboard
import copy


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
