import socket
import json
import struct
import random
from src.negamax import move


def inscription(
    AIname: str,
    matricule: list[int, int],
    servIPadress: str,
    clientPort=8888,
    serverPort=3000,
) -> None:
    """register our info to the game server

    Args:
        AIname (str): name of the AI
        matricule (list[int, int]): list of two numbers of 5 digits
        servIPadress (str): IP adress of the server we want to play in
        clientPort (int, optional): client communication free port. Defaults to 8888.
        serverPort (int, optional): server port. Defaults to 3000.
    """

    inscription_data = {
        "request": "subscribe",
        "port": clientPort,
        "name": AIname,
        "matricules": [matricule[0], matricule[1]],
    }
    # tell the server to communicate with clientPort
    with socket.socket() as s:
        s.connect((servIPadress, serverPort))
        message = json.dumps(inscription_data).encode("utf-8")
        s.send(struct.pack("I", len(message)))
        s.send(message)
        response = s.recv(32).decode("utf-8")
        print(response)  # should recieve 'OK' form the server


def pong_message() -> json:
    """construct the pong massage to send

    Returns:
        json: encoded json with pong massage
    """

    pong_data = {"response": "pong"}

    return json.dumps(pong_data).encode("utf-8")


def move_message(boardState: dict, strategy: bool, time_limit: float = 2.5) -> json:
    """construct the move message to send

    Args:
        boardState (dict): current state of the game
        strategy (bool): algorithm (True) or random (False)
        time_limit (float): must send after this limit. efaults to 2.5.

    Returns:
        json: encoded json with move message
    """

    move_to_play = move(boardState, strategy, time_limit)
    fun_message = random.choice(["subscribed to my OnlyFans !", "you're ass!"])

    move_data = {
        "response": "move",
        "move": move_to_play,
        "message": fun_message,
    }

    return json.dumps(move_data).encode("utf-8")


def server_communication(clientPort=8888, strategy=False, time_limit: float = 2.5) -> None:
    """communicate with the server, must desactivate 2 fire-wall in "par feu windows defender" do receive massages

    Args:
        clientPort (int, optional): client communication free port. Defaults to 8888.
        strategy (bool, optional): algorithm (True) or random (False). Defaults to False.
        time_limit (float, optional): must send after this limit. Defaults to 2.5.
    """

    with socket.socket() as ls:
        ls.bind(("0.0.0.0", clientPort))  # localhost = "0.0.0.0"
        ls.listen()
        ls.settimeout(0.5)
        while True:
            try:
                client, address = ls.accept()
                print(f"connection from {address}")
                with client:
                    # check the length of the massage to recieve
                    len_info = client.recv(4)
                    len_mes = struct.unpack("I", len_info)[0]
                    message = client.recv(len_mes)
                    while len(message) < len_mes:
                        message += client.recv(len_mes - len(message))

                    client_message = message.decode("utf-8")  # should receive ping or state
                    client_message_dict = json.loads(client_message)

                    # respond to ping request (to make sure we are still connected)
                    if client_message_dict["request"] == "ping":
                        pong = pong_message()
                        client.send(struct.pack("I", len(pong)))
                        client.send(pong)  # sould send pong

                    # respond to play request and show possible error messages
                    elif client_message_dict["request"] == "play":
                        boardState = client_message_dict["state"]
                        mm = move_message(boardState, strategy, time_limit)
                        client.send(struct.pack("I", len(mm)))
                        client.send(mm)  # sould send the move

                        for error in client_message_dict["errors"]:
                            error.pop("state", None)
                        print(client_message_dict["errors"])

            except socket.timeout:
                pass
