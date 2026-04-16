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
        "port": 8888,
        "name": "GIGA BYTE  BLYAT",
        "matricules": ["24087", "24092"]
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
    current = recu['state']['current']
    if current == 0:
        Pawncolor = 'dark'
        print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")
        ennemi = recu['state']['players'][1]
    else:
        Pawncolor = 'light'
        print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")
        ennemi = recu['state']['players'][0]
    
    pawnPos, start = FindPawn(headColor,iniState,Pawncolor)
    moveToPlay = Move(pawnPos,current,start)
    Sendmove(s,moveToPlay,ennemi)
    
    
def FindPawn(headColor, iniState,Pawncolor) :
    for i in range(8):
        for j in range(8):
            if iniState[i][j][1] != None :
                print(iniState[i][j][1])
                if headColor is None:
                    a =random.randint(0,7)
                    return [7,a], 'start'
                elif headColor in  iniState[i][j][1][0] and Pawncolor in  iniState[i][j][1][1] :
                    print(i,j)
                    pos =[i,j]
                    return pos, "going"
    raise ValueError("no Pawn found :(")

def Move(JEF_towerPosition : list, JEF_currentInStateJson : int, play : str) -> list:

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

    return [currentPosition, finalPosition]

def Sendmove(s,the_move_played,name):
    fun_message = [f"{name} did a bold move !", f"{name} just subscribed to my OnlyFans !", f"domain expansion: 'Nah, I'd win ",
                   f"BOT LOBBY", f"gg ez", f"pickle", f"what is {name} even doing -_-", f"when is the competition starting ?",
                   f"You tried at least", f"BOMBACLAT !", f"Waiter ! waiter ! more {name}'s bad moves !",
                   f"Am I real ?", f"{name} CPU is burning", f"SMASH, next question", f"{name} just did a 6 7 !", f"No Bitches?",
                   f"{name} plays LoL everyday", f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)"
                   ,f"Are we done ?"]
    Fun_message = fun_message[random.randint(0,len(fun_message))]
    Move ={
   "response": "move",
   "move": the_move_played,
   "message": Fun_message
    }
    send_json(s,Move)

#############################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls = socket.socket()
ls.bind(("0.0.0.0",8888))

try:
    address = ('10.0.0.144', 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
    print(f"connected to {address}")
except OSError :
    print ("Serveur introuvable , connexion impossible .")

inscription(s)
print(recv_json(s))

ls.settimeout(2)
ls.listen()
while True:
    try: 
        client, adress = ls.accept()
        with client:
            recu =recv_json(client)
            print(recu)
            if recu['request'] == "ping":  #ERROR I just want the word ping 
                pingRequest(client)
            if recu['request'] == "play":
                print('PLAY')
                print(f"il reste {recu["lives"]} vie ")
                PLAY(s,recu)
                # iniState = recu['state']['board']
                # headColor = recu['state']['color']
                # print(f"headColor is {headColor}, and type {type(headColor)}")
                # if recu['state']['current'] == 0:
                #     Pawncolor = 'dark'
                #     print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")
                # else:
                #     Pawncolor = 'light'
                #     print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")

                

    except socket.timeout:
        pass