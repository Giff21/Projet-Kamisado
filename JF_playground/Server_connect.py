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
        "name": "MR BAD MOVE",
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
    
    pawnPos = FindPawn(headColor,iniState,Pawncolor,current)[2]
    currentPosition,finalPosition = Move(pawnPos,current,random.choice(['forward', 'Rdiagonal', 'Ldiagonal']))
    Sendmove(s,currentPosition,finalPosition,ennemi)
    print("MOVE SENT")
    
def FindPawn(headColor, iniState,Pawncolor,current) :
    darkPawn=[]
    lightPawn=[]
    if headColor == None or headColor == 'n':
        if current == 0:
            a =random.randint(0,7)
            print(f"[7,{a}]")
            pos = [7,a]
        else:
            a = random.randint(0,7)
            print(f"[0,{a}]")
            pos = [0,a]
    for i in range(8):
        for j in range(8):
            case = iniState[i][j][1]
            if isinstance(case, list):
                color, pawn = case
                if headColor == color and Pawncolor == pawn :
                    print(f"[{i},{j}] is {headColor} and {Pawncolor}")
                    pos =[i,j]
                    
                if pawn == 'dark':
                    darkPawn.append([i,j])
                if pawn == 'light':
                    lightPawn.append([i,j])
             
    return [darkPawn,lightPawn,pos]
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
        
        if  currentPosition[0] == finalPosition[0] or currentPosition[1] == finalPosition[1]:
            finalPosition = [finalPosition[0]-1, finalPosition[1]]

    elif JEF_currentInStateJson == 1:
        if play == 'forward':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]]
        if play == 'Rdiagonal':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]-random.randint(0,7-currentPosition[1])]
        if play == 'Ldiagonal':
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]+random.randint(0,7-currentPosition[1])]
        
        if currentPosition[0] == finalPosition[0] or currentPosition[1] == finalPosition[1]:
            finalPosition = [finalPosition[0]+1, finalPosition[1]+1]

    print(play,":",currentPosition,",",finalPosition)
    return currentPosition, finalPosition

def Sendmove(ls,currentPosition,finalPos,name):
    fun_message = [f"{name} did a bold move !", f"{name} just subscribed to my OnlyFans !", f"domain expansion: Nah, I'd win ",
                   f"BOT LOBBY", f"gg ez", f"pickle", f"what is {name} even doing -_-", f"when is the competition starting ?",
                   f"You tried at least", f"BOMBACLAT !", f"Waiter ! waiter ! more {name}'s bad moves !",
                   f"Am I real ?", f"{name} CPU is burning", f"SMASH, next question", f"{name} just did a 6 7 !", f"No Bitches?",
                   f"{name} plays LoL everyday", f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)",f"+1 for the funny message ? ;)"
                   ,f"Are we done ?", f"simply better", f"YOU NOOB",f"Trust me, I'm an engineer", f"Trust me bro",f"go play the tutorial",
                   f"your mandatory prostate inspection is coming", f"I am inevitable", f"{name} is a furry", f"My name is jefff"]

    Fun_message = random.choice(fun_message)
    Move ={
   "response": "move",
   "move": [currentPosition,finalPos],
   "message": Fun_message
    }
    send_json(ls,Move)

#############################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls = socket.socket()
ls.bind(("0.0.0.0",8888))

try:
    address = ('172.17.10.54', 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
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
            if recu['request'] == "ping":  
                pingRequest(client)
            if recu['request'] == "play":
                print('######PLAY######')
                print('error:',recu['errors'])
                print(f"il reste {recu["lives"]} vie ")
                PLAY(client,recu)
  
    except socket.timeout:
        pass