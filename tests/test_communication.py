from src.communication import pong_message
from src.communication import move_message
import json
import copy
from tests.board_test import tboard


def test_pong_message():
    message = pong_message().decode("utf-8")
    client_message = json.loads(message)
    assert client_message == {"response": "pong"}


def test_move_message():
    board = copy.deepcopy(tboard)
    message = move_message(board, strategy=False, time_limit=0.5).decode("utf-8")
    client_message = json.loads(message)
    assert client_message["response"] == "move"
    assert len(client_message["move"]) == 2
    assert client_message["message"] in ["subscribed to my OnlyFans !", "you're ass!"]
