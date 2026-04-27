import socket
import json
import struct
import random
from ai_move import move


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
        matricule (list[int, int]): list of the number of 5 digits
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
    # send inscription info to the server, tell the server to communicate with clientPort
    with socket.socket() as s:
        s.connect((servIPadress, serverPort))
        message = json.dumps(inscription_data).encode("utf-8")
        s.send(struct.pack("I", len(message)))
        s.send(message)
        response = s.recv(32).decode("utf-8")
        print(response)  # should recieve 'OK' form the server


def pong_message() -> json:
    """pong massage

    Returns:
        json: encoded json with pong massage
    """

    pong_data = {"response": "pong"}

    return json.dumps(pong_data).encode("utf-8")


def move_message(boardState: dict, strategy: bool) -> json:
    """use the board and move function to construct the tamplate to send

    Args:
        boardState (dict): current state of the game

    Returns:
        json: encoded json with move message
    """

    move_to_play = move(boardState, strategy)
    fun_message = random.choice(["subscribed to my OnlyFans !", "you're ass!"])

    move_data = {
        "response": "move",
        "move": move_to_play,  # must be [[1,2],[3,4]]
        "message": fun_message,
    }

    return json.dumps(move_data).encode("utf-8")


def server_communication(clientPort=8888, strategy=False) -> None:
    """communicate with the server, send pong if ping request and send the move. Must desactivate 2 fire-wall in "par feu windows defender" do receive massages

    Args:
        clientPort (int, optional): client communication free port. Defaults to 8888.
    """

    with socket.socket() as ls:
        ls.bind(("0.0.0.0", clientPort))
        ls.listen()
        ls.settimeout(0.5)
        while True:
            try:
                client, address = ls.accept()
                print(f"connection from {address}")
                with client:
                    # check the length of the massage to recieve (encoded json) and decode
                    len_info = client.recv(4)
                    len_mes = struct.unpack("I", len_info)[0]
                    message = client.recv(len_mes)
                    while len(message) < len_mes:
                        message += client.recv(len_mes - len(message))
                    # should receive ping or the game state
                    client_message = message.decode("utf-8")
                    client_message_dict = json.loads(client_message)

                    # respond to ping request (to make sure we are still connected)
                    if client_message_dict["request"] == "ping":
                        pong = pong_message()
                        client.send(struct.pack("I", len(pong)))
                        client.send(pong)  # sould send pong

                    # respond to play request and show possible error messages
                    elif client_message_dict["request"] == "play":
                        boardState = client_message_dict["state"]
                        mm = move_message(boardState, strategy)
                        client.send(struct.pack("I", len(mm)))
                        client.send(mm)  # sould send the move
                        for error in client_message_dict["errors"]:
                            error.pop("state", None)
                        print(client_message_dict["errors"])

            except socket.timeout:
                pass
