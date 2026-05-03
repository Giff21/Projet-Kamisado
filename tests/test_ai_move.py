# run python -m pytest -v in the terminal to check the tests

from src.ai_move import possible_move


# dark movement test
def test_dark_forward():
    dark = [[3, 2]]
    light = [[1, 2]]
    result = possible_move(dark, light, [3, 2], 0)
    assert [2, 2] in result


def test_dark_diagonal_right():
    dark = [[2, 2]]
    light = []
    result = possible_move(dark, light, [2, 2], 0)
    assert [1, 3] in result
    assert [0, 4] in result


def test_dark_diagonal_left():
    dark = [[2, 2]]
    light = []
    result = possible_move(dark, light, [2, 2], 0)
    assert [1, 1] in result
    assert [0, 0] in result


# light movement test
def test_light_forward():
    dark = [[6, 5]]
    light = [[4, 5]]
    result = possible_move(dark, light, [4, 5], 1)
    assert [5, 5] in result


def test_light_diagonal_right():
    dark = []
    light = [[5, 5]]
    result = possible_move(dark, light, [5, 5], 1)
    assert [6, 4] in result
    assert [7, 3] in result


def test_light_diagonal_left():
    dark = []
    light = [[5, 5]]
    result = possible_move(dark, light, [5, 5], 1)
    assert [6, 6] in result
    assert [7, 7] in result


# respect the board dimentions
def test_dark_top_row_forward_move():
    dark = [[0, 4]]
    light = []
    result = possible_move(dark, light, [0, 4], 0)
    for pos in result:
        assert pos[0] >= 0  # can't be négative


def test_dark_left_edge():
    dark = [[4, 0]]
    light = []
    result = possible_move(dark, light, [4, 0], 0)
    for pos in result:
        assert pos[1] >= 0


def test_dark_right_edge():
    dark = [[4, 7]]
    light = []
    result = possible_move(dark, light, [4, 7], 0)
    for pos in result:
        assert pos[1] <= 7


def test_light_bottom_row_forward_move():
    dark = []
    light = [[7, 0]]
    result = possible_move(dark, light, [7, 0], 1)
    for pos in result:
        assert pos[0] >= 7  # can't be over the board dimentions


def test_light_left_edge():
    dark = []
    light = [[5, 0]]
    result = possible_move(dark, light, [5, 0], 1)
    for pos in result:
        assert pos[1] >= 0


def test_light_right_edge():
    dark = []
    light = [[5, 7]]
    result = possible_move(dark, light, [5, 7], 1)
    for pos in result:
        assert pos[1] <= 7


# test to stay on the same position if not move available
def test_no_move_dark():
    dark = [[0, 0]]
    light = []
    result = possible_move(dark, light, [0, 0], 0)
    assert result == [[0, 0], [0, 0]]


def test_no_move_light():
    dark = []
    light = [[7, 7]]
    result = possible_move(dark, light, [7, 7], 1)
    assert result == [[7, 7], [7, 7]]
