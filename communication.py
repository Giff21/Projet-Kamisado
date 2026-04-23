import socket
import json
import struct
import random
from AI_move import move
from Pawn_finder import FindPawn
from AI_move import PossibleMove


def inscription( AIname: str, matricule: list[int,int], servIPadress: str, clientPort=8888, serverPort=3000):
    """Return nothing
    descr : register our info to the game server
    """

    inscription_data = {
    "request": "subscribe",
    "port": clientPort,
    "name": AIname,
    "matricules": [matricule[0], matricule[1]]
    }

    with socket.socket() as s:
        s.connect((servIPadress, serverPort))
        message = json.dumps(inscription_data).encode('utf-8')
        s.send(struct.pack("I", len(message)))
        s.send(message)
        response = s.recv(32).decode('utf-8')
        print(response) #should recieve 'OK' form the server


def pongMessage() -> json:
    """Return the encoded json with "pong" """

    pong_data = {
    "response": "pong"
    }

    return json.dumps(pong_data).encode('utf-8')


def moveMessage(boardState: dict) -> json:
    """Return the encoded json with the move to do

    agr : dict of the board state
    descr : take board use the move function to find a moveToPlay and construct the tamplate to send
    """
    
    PossibleMove(boardState)
    FindPawn(boardState)
    moveToPlay = move(boardState)
    fun_message = random.choice(["subscribed to my OnlyFans !", "you're ass!"])

    move_data = {
    "response": "move",
    "move": moveToPlay, #must be [[1,2],[3,4]]
    "message": fun_message
    }

    return json.dumps(move_data).encode('utf-8')


def serverCom(clientPort=8888):
    """Return nothing

    descr : communicate with the server - send pong if ping recieved then, take the board state and send the move
    must do : desactivate 2 fire-wall in par feu windows defender do receive massages
    
    """
    with socket.socket() as ls:
        ls.bind(('0.0.0.0', clientPort))
        #print(f"listen on {clientPort}")
        ls.listen()
        ls.settimeout(0.5)
        while True:
            try:
                client, address = ls.accept()
                print(f"connection from {address}")
                with client:
                    len_info = client.recv(4)
                    len_mes = struct.unpack("I", len_info)[0]
                    message = client.recv(len_mes) #sould receive ping
                    while len(message) < len_mes:
                        message += client.recv(len_mes - len(message))
                    client_message = message.decode('utf-8')
                    
                    client_message_dict = json.loads(client_message)
                    #print(client_message_dict)

                    if client_message_dict["request"] == "ping":
                        client.send(struct.pack("I", len(pongMessage())))
                        client.send(pongMessage()) #sould send pong
                        #print(json.loads(pongMessage()))

                    elif client_message_dict["request"] == "play":
                        boardState = client_message_dict["state"]
                        mm = moveMessage(boardState)
                        client.send(struct.pack("I", len(mm)))
                        client.send(mm) #sould send the move
                        print(client_message_dict["errors"])


            except socket.timeout:
                pass
