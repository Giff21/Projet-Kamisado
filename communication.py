import socket
import json
import struct

def inscription(IPadress: str, clientPort: int, AIname: str, matricule: list[int,int], serverPort: int):
    """
    register our info to the game server
    """

    inscription_data = {
    "request": "subscribe",
    "port": clientPort,
    "name": AIname,
    "matricules": [matricule[0], matricule[1]]
    }

    with socket.socket() as s:
        s.connect((IPadress, serverPort))
        message = json.dumps(inscription_data).encode('utf-8')
        s.send(struct.pack("I", len(message)))
        s.send(message)
        response = s.recv(32).decode('utf-8')
        print(response) #should recieve 'OK' form the server

def moveMessage(move: list) -> json:
    """Return the encoded json with the move to do

    take the move to do and construct the tamplate to send
    """
    move_data = {
    "response": "move",
    "move": move,
    "message": "Fun message"
    }

    return json.dumps(move_data).encode('utf-8')
