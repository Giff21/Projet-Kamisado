# tests for the negamax file
from src.negamax import winner, heurestic, game_over, apply, negamax, move
from src.pawn_finder import find_pawn
import pytest

@pytest.fixture
def Recu3():  # light win
  return {"request": "play",
   "lives": 3,
   "errors": "list_of_errors",
   "state":{"board": [[
      ["orange", "null"],
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
      ["yellow", ["green", "dark"]],
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
      ["green", ["pink", "light"]],
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
def Recu4():  # dark win
  return {"request": "play",
   "lives": 3,
   "errors": "list_of_errors",
   "state":{"board": [[
      ["orange", ["green", "dark"]],
      ["blue", ["orange", "light"]],
      ["purple", ["green", "light"]],
      ["pink", ["red", "light"]],
      ["yellow", ["purple", "light"]],
      ["red", ["blue", "light"]],
      ["green", ["brown", "light"]],
      ["brown", ["yellow", "light"]]
    ],
    [
      ["red", ["pink", "light"]],
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
      ["red", ]
    ],
    [
      ["brown", ["yellow", "dark"]],
      ["green", "null"],
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

def test_winner():
  darkPawnWin = [[0,0],[7,0],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]]
  darkPawn = [[5,1],[7,0],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]]
  lightPawnWin = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[7,1]]
  lightPawn = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[1,0]]

  assert winner(darkPawnWin,lightPawn) == 0, 'dark not in row 0 (win row)'
  assert winner(darkPawn,lightPawnWin) == 1, 'light not in row 7 (win row)'
  assert winner(darkPawn,lightPawn) == None, 'winner detected when no winner pawn pos'

def test_heuristic():
  