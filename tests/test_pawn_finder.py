# tests for the pawn_finder file
from src.pawn_finder import find_pawn
import pytest

#example of recieved message from the server with recu2 being a modification of recu1
#representing a played game state
@pytest.fixture
def recu1():
  return {
   "request": "play",
   "lives": 3,
   "errors": "list_of_errors",
   "state":{"board": [[
      ["orange", ["pink", "light"]],
      ["blue", ["orange", "light"]],
      ["purple", ["green", "light"]],
      ["pink", ["red", "light"]],
      ["yellow", ["purple", "light"]],
      ["red", ["blue", "light"]],
      ["green", ["brown", "light"]],
      ["brown", ["yellow", "light"]]
    ],
    [
      ["red", "null"],
      ["orange", "null"],
      ["pink", "null"],
      ["green", "null"],
      ["blue", "null"],
      ["yellow", "null"],
      ["brown", "null"],
      ["purple", "null"]
    ],
    [
      ["green", "null"],
      ["pink", "null"],
      ["orange", "null"],
      ["red", "null"],
      ["purple", "null"],
      ["brown", "null"],
      ["yellow", "null"],
      ["blue", "null"]
    ],
    [
      ["pink", "null"],
      ["purple", "null"],
      ["blue", "null"],
      ["orange", "null"],
      ["brown", "null"],
      ["green", "null"],
      ["red", "null"],
      ["yellow", "null"]
    ],
    [
      ["yellow", "null"],
      ["red", "null"],
      ["green", "null"],
      ["brown", "null"],
      ["orange", "null"],
      ["blue", "null"],
      ["purple", "null"],
      ["pink", "null"]
    ],
    [
      ["blue", "null"],
      ["yellow", "null"],
      ["brown", "null"],
      ["purple", "null"],
      ["red", "null"],
      ["orange", "null"],
      ["pink", "null"],
      ["green", "null"]
    ],
    [
      ["purple", "null"],
      ["brown", "null"],
      ["yellow", "null"],
      ["blue", "null"],
      ["green", "null"],
      ["pink", "null"],
      ["orange", "null"],
      ["red", "null"]
    ],
    [
      ["brown", ["yellow", "dark"]],
      ["green", ["green", "dark"]],
      ["red", ["orange", "dark"]],
      ["yellow", ["purple", "dark"]],
      ["pink", ["red", "dark"]],
      ["purple", ["brown", "dark"]],
      ["blue", ["blue", "dark"]],
      ["orange", ["pink", "dark"]]
    ]
  ],
  "color": None,
  "current": 0,
  "players": ["LUR", "FKY"]
}
}

@pytest.fixture
def recu2():
  return {
   "request": "play",
   "lives": 3,
   "errors": "list_of_errors",
   "state":{"board": [[
      ["orange", "null"],
      ["blue", ["orange", "light"]],
      ["purple","null"],
      ["pink", ["red", "light"]],
      ["yellow","null"],
      ["red", ["blue", "light"]],
      ["green", "null"],
      ["brown", ["yellow", "light"]]
    ],
    [
      ["red", ["pink", "light"]],
      ["orange", "null"],
      ["pink",  ["green", "light"]],
      ["green", "null"],
      ["blue",  ["purple", "light"]],
      ["yellow", "null"],
      ["brown", ["brown", "light"]],
      ["purple", "null"]
    ],
    [
      ["green", "null"],
      ["pink", "null"],
      ["orange", "null"],
      ["red", "null"],
      ["purple", "null"],
      ["brown", "null"],
      ["yellow", "null"],
      ["blue", "null"]
    ],
    [
      ["pink", "null"],
      ["purple", "null"],
      ["blue", "null"],
      ["orange", "null"],
      ["brown", "null"],
      ["green", "null"],
      ["red", "null"],
      ["yellow", "null"]
    ],
    [
      ["yellow", "null"],
      ["red", "null"],
      ["green", "null"],
      ["brown", "null"],
      ["orange", "null"],
      ["blue", "null"],
      ["purple", "null"],
      ["pink", "null"]
    ],
    [
      ["blue", "null"],
      ["yellow", "null"],
      ["brown", "null"],
      ["purple", "null"],
      ["red", "null"],
      ["orange", "null"],
      ["pink", "null"],
      ["green", "null"]
    ],
    [
      ["purple", ["yellow", "dark"]],
      ["brown", "null"],
      ["yellow", ["orange", "dark"]],
      ["blue", "null"],
      ["green", ["red", "dark"]],
      ["pink", "null"],
      ["orange", ["blue", "dark"]],
      ["red", "null"]
    ],
    [
      ["brown", "null"],
      ["green", ["green", "dark"]],
      ["red", "null"],
      ["yellow", ["purple", "dark"]],
      ["pink", "null"],
      ["purple", ["brown", "dark"]],
      ["blue", "null"],
      ["orange", ["pink", "dark"]]
    ]
  ],
  "color": 'red',
  "current": 1,
  "players": ["LUR", "FKY"]
}
}

def test_type_check(recu1):
    boardState = recu1['state']
    result = find_pawn(boardState)

    assert isinstance(result,tuple), 'return type is not tuple'
    assert isinstance(result[0],list), 'dark_pawn type is not list'
    assert isinstance(result[1],list), 'light_pawn type is not list'
    assert isinstance(result[2],list), 'chosen_pos is not list'
    assert isinstance(result[3],list),  'current_side is not int'

def test_dark_pawn_pos(recu1,recu2):
    boardState1 = recu1['state']
    boardState2 = recu2['state']
    dark_pawn_pos1 = [[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]
    dark_pawn_pos2 = [[6, 0], [7, 1], [6, 2], [7, 3], [6, 4], [7, 5], [6, 6], [7, 7]]
    result1 = find_pawn(boardState1)
    result2 = find_pawn(boardState2)

    assert dark_pawn_pos1 in result1[0], 'list of dark_pawn_pos1 is not correct'
    assert dark_pawn_pos2 in result2[0], 'list of dark_pawn_pos2 is not correct'

def test_light_pawn_pos(recu1,recu2):
    boardState1 = recu1['state']
    boardState2 = recu2['state']
    light_pawn_pos1 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
    light_pawn_pos2 = [[1, 0], [0, 1], [1, 2], [0, 3], [1, 4], [0, 5], [1, 6], [0, 7]]
    result1 = find_pawn(boardState1)
    result2 = find_pawn(boardState2)

    assert light_pawn_pos1 in result1[1], 'list of light_pawn_pos1 is not correct'
    assert light_pawn_pos2 in result2[1], 'list of light_pawn_pos2 is not correct'

def test_chosen_pawn_red(recu2):
    boardState = recu2['state']
    result = find_pawn(boardState)

    assert [0,3] in result[2], 'chosen pawn is not the [red,light] pawn'

def test_chose_pawn_null(recu1):
    boardState = recu1['state']
    result = find_pawn(boardState)

    assert [7,type(int)] in result[2], 'chosen pawn is not on line 7 (dark line)'

def test_own_color(recu1,recu2):
    boardState1 = recu1['state']
    boardState2 = recu2['state']
    result1 = find_pawn(boardState1)
    result2 = find_pawn(boardState2)

    assert 0 in result1[3], 'own color is not dark'
    assert 1 in result2[3], 'own color is not light'

