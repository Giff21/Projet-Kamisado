# import random
# recu ={
#    "request": "play",
#    "lives": 3,
#    "errors": "list_of_errors",
#    "state":{
#   "board": [[
#       ["orange", ["pink", "light"]],
#       ["blue", ["orange", "light"]],
#       ["purple", ["green", "light"]],
#       ["pink", ["red", "light"]],
#       ["yellow", ["purple", "light"]],
#       ["red", ["blue", "light"]],
#       ["green", ["brown", "light"]],
#       ["brown", ["yellow", "light"]]
#     ],
#     [
#       ["red", "null"],
#       ["orange", "null"],
#       ["pink", "null"],
#       ["green", "null"],
#       ["blue", "null"],
#       ["yellow", "null"],
#       ["brown", "null"],
#       ["purple", "null"]
#     ],
#     [
#       ["green", "null"],
#       ["pink", "null"],
#       ["orange", "null"],
#       ["red", "null"],
#       ["purple", "null"],
#       ["brown", "null"],
#       ["yellow", "null"],
#       ["blue", "null"]
#     ],
#     [
#       ["pink", "null"],
#       ["purple", "null"],
#       ["blue", "null"],
#       ["orange", "null"],
#       ["brown", "null"],
#       ["green", "null"],
#       ["red", "null"],
#       ["yellow", "null"]
#     ],
#     [
#       ["yellow", "null"],
#       ["red", "null"],
#       ["green", "null"],
#       ["brown", "null"],
#       ["orange", "null"],
#       ["blue", "null"],
#       ["purple", "null"],
#       ["pink", "null"]
#     ],
#     [
#       ["blue", "null"],
#       ["yellow", "null"],
#       ["brown", "null"],
#       ["purple", "null"],
#       ["red", "null"],
#       ["orange", "null"],
#       ["pink", "null"],
#       ["green", "null"]
#     ],
#     [
#       ["purple", "null"],
#       ["brown", "null"],
#       ["yellow", "null"],
#       ["blue", "null"],
#       ["green", "null"],
#       ["pink", "null"],
#       ["orange", "null"],
#       ["red", "null"]
#     ],
#     [
#       ["brown", ["yellow", "dark"]],
#       ["green", ["green", "dark"]],
#       ["red", ["orange", "dark"]],
#       ["yellow", ["purple", "dark"]],
#       ["pink", ["red", "dark"]],
#       ["purple", ["brown", "dark"]],
#       ["blue", ["blue", "dark"]],
#       ["orange", ["pink", "dark"]]
#     ]
#   ],
#   "color": 'red',
#   "current": 0,
#   "players": ["LUR", "FKY"]
# }
# }

# def FindPawn(headColor: str, iniState:list,pawnColor : str)  : #  str) -> tuple : 
#     for i in range(8):
#         for j in range(8):
#             if iniState[i][j][1] != 'null' :
#                 #print(iniState[i][j][1])
#                 if headColor == 'null':
#                     a =random.randint(0,8)
#                     return print('start'), print((8,a))
#                 elif headColor in  iniState[i][j][1][0] and Pawncolor in  iniState[i][j][1][1] :
#                     print(i,j)
#                     pos =[i,j+1]
#                     return print(pos)


# def Sendmove(s,the_move_played):
#     Move ={
#    "response": "move",
#    "move": the_move_played,
#    "message": "Fun message"
#     }
#     return print(Move)


# print('PLAY')
# print(f"il reste {recu["lives"]} vie ")
# iniState = recu['state']['board']
# headColor = recu['state']['color']
# print("current:",recu['state']['current'])
# print(f"headColor is {headColor}, and type {type(headColor)}")
# if recu['state']['current'] == 0: # ==name of AI
#     Pawncolor = 'dark'
#     print(f"PawnColor is {Pawncolor}, and type type(Pawncolor)")
# else:
#     Pawncolor = 'light'
#     print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")
# FindPawn(headColor,iniState,Pawncolor)

# #FindPawn(headColor,iniState,Pawncolor)

import socket
import json
import struct
import random

def send_json(s,data: dict) -> None:  #https://oneuptime.com/blog/post/2026-03-20-json-over-ipv4-sockets-python/view
    """Serialize data to JSON and send with a 4-byte length prefix."""
    message = json.dumps(data).encode("utf-8")
    # Pack the length as a 4-byte big-endian unsigned integer
    header = struct.pack("<I", len(message))
    s.send(header + message)

def recv_json(sock: socket.socket) -> dict:
    """Receive a length-prefixed JSON message from the socket."""
    # Read exactly 4 bytes for the length header
    raw_len = recvn(sock,4)

    if not raw_len:
        raise ConnectionError("Connection closed while reading header")
    
    msg_len = struct.unpack("<I", raw_len)[0] # "<I" = Little-endian
    print(msg_len)
    # Read exactly msg_len bytes for the payload
    raw_payload = recvn(sock,msg_len)
    if not raw_payload:
        raise ConnectionError("Connection closed while reading payload")

    return json.loads(raw_payload.decode("utf-8"))

def recvn(s:socket.socket, n: int) -> bytes:
    """Read exactly n bytes from the socket."""
    buf = b""
    while len(buf) < n:
        chunk = s.recv(n - len(buf))
        if not chunk:
            return b""
        buf += chunk
    return buf

def inscription(s):
    inscription_Json ={
        "request": "subscribe",
        "port": 8887,
        "name": "Maelle",
        "matricules": ["00000", "22222"]
    }
    send_json(s,inscription_Json)
    print("insciption sent")

def pingRequest(clientSock):
    pong ={
    "response": "pong"
    }
    send_json(clientSock,pong)
    print('ping sent')

def PLAY(s,recu):
    iniState = recu['state']['board']
    headColor = recu['state']['color']
    print(f"Headcolor is {headColor}")
    current = recu['state']['current']
    if current == 0:
        Pawncolor = 'dark'
        print(f"PawnColor is {Pawncolor}")
        ennemi = recu['state']['players'][1]
    else:
        Pawncolor = 'light'
        print(f"PawnColor is {Pawncolor}")
        ennemi = recu['state']['players'][0]
    
    pawnPos = FindPawn(headColor,iniState,Pawncolor,current)
    currentPosition,finalPosition = Move(pawnPos,current,random.choice(['forward', 'Rdiagonal', 'Ldiagonal']))
    Sendmove(s,currentPosition,finalPosition,ennemi)
    print("MOVE SENT")
    
    
def FindPawn(headColor, iniState,Pawncolor,current) :
    for i in range(8):
        for j in range(8):
            #if iniState[i][j][1] != None :
            #   print("iniState is not none")
                if headColor == None:
                    if current == 0:
                        a =random.randint(0,7)
                        print(f"[0,{a}]")
                        return [0,a]
                    elif current == 1:
                        a = random.randint(0,7)
                        print(f"[7,{a}]")
                        return [7,a]
                elif headColor in  iniState[i][j][1][0] and Pawncolor in  iniState[i][j][1][1] :
                    print(f"[i,j] is {headColor} and {Pawncolor}")
                    pos =[i,j]
                    return pos
    raise ValueError("no Pawn found :(")

def Move(JEF_towerPosition : list, JEF_currentInStateJson : int, play : str):

    currentPosition = [JEF_towerPosition[0], JEF_towerPosition[1]]
    
    if JEF_currentInStateJson == 0:
        if play == 'forward':
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]]
        if play == 'Rdiagonal':
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]+random.randint(0,currentPosition[1])]
        if play == 'Ldiagonal':
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]-random.randint(0,currentPosition[1])]

    elif JEF_currentInStateJson == 1:
        if play == 'forward':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]]
        if play == 'Rdiagonal':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]-random.randint(0,7-currentPosition[1])]
        if play == 'Ldiagonal':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]+random.randint(0,7-currentPosition[1])]

    return currentPosition, finalPosition

def Sendmove(s,currentPosition,finalPos,name):
    fun_message = [f"{name} did a bold move !", f"{name} just subscribed to my OnlyFans !", f"domain expansion: 'Nah, I'd win ",
                   f"BOT LOBBY", f"gg ez", f"pickle", f"what is {name} even doing -_-", f"when is the competition starting ?",
                   f"You tried at least", f"BOMBACLAT !", f"Waiter ! waiter ! more {name}'s bad moves !",
                   f"Am I real ?", f"{name} CPU is burning", f"SMASH, next question", f"{name} just did a 6 7 !", f"No Bitches?",
                   f"{name} plays LoL everyday", f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)"
                   ,f"Are we done ?"]
#   Fun_message = fun_message[random.randint(0,len(fun_message))]
    print(f"[{currentPosition}, {finalPos}]")
    Move ={
   "response": "move",
   "move": [currentPosition,finalPos],
   "message": "Fun_message"
    }
    send_json(s,Move)

#############################################

s = socket.socket()
ls = socket.socket()
ls.bind(("0.0.0.0",8887))

try:
    address = ('172.17.10.35', 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
    print(f"connected to {address}")
except OSError :
    print ("Serveur introuvable , connexion impossible .")

inscription(s)
print(recv_json(s))

ls.settimeout(0.5)
ls.listen()
while True:
    try: 
        client, adress = ls.accept()
        with client:
            recu =recv_json(client)
            #print(recu)
            if recu['request'] == "ping":  #ERROR I just want the word ping 
                pingRequest(client)
            if recu['request'] == "play":
                print(f"PLAY : il reste {recu["lives"]} vie ")
                PLAY(client,recu)
            
    except socket.timeout:
        pass