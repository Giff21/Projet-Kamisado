import pytest
from ai_move import possible_move


# dark movement test
def test_dark_forward():
    dark = [[4, 4]]
    light = []
    result = possible_move(dark, light, [4, 4], 0)
    assert [3, 4] in result
    assert [2, 4] in result
    assert [1, 4] in result
    assert [0, 4] in result


def test_dark_diagonal_right():
    dark = [[4, 4]]
    light = []
    result = possible_move(dark, light, [4, 4], 0)
    assert [3, 5] in result
    assert [2, 6] in result
    assert [1, 7] in result


def test_dark_diagonal_left():
    dark = [[4, 4]]
    light = []
    result = possible_move(dark, light, [4, 4], 0)
    assert [3, 3] in result
    assert [2, 2] in result
    assert [1, 1] in result
    assert [0, 0] in result


# light movement test
def test_light_forward():
    dark = []
    light = [[3, 3]]
    result = possible_move(dark, light, [3, 3], 1)
    assert [4, 3] in result
    assert [5, 3] in result
    assert [6, 3] in result
    assert [7, 3] in result


def test_light_diagonal_right():
    dark = []
    light = [[3, 3]]
    result = possible_move(dark, light, [3, 3], 1)
    assert [4, 2] in result
    assert [5, 1] in result
    assert [6, 0] in result


def test_light_diagonal_left():
    dark = []
    light = [[3, 3]]
    result = possible_move(dark, light, [3, 3], 1)
    assert [4, 4] in result
    assert [5, 5] in result
    assert [6, 6] in result
    assert [7, 7] in result
