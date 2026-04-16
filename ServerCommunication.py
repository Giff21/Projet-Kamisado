import socket
import struct
import json
import random


#----------- send the connection message in TCP------------
serverAddress = ('172.17.10.46', 3000)  #ip and port of teacher
myAdress = ('0.0.0.0', 8888)    #my IP and listening port

my_data ={
    "request": "subscribe",
    "port": 8888,
    "name": "Anita Max Wynn",
    "matricules": ["24092", "24087"]
}

s = socket.socket()
s.connect(serverAddress)
message = json.dumps(my_data).encode('utf-8')
s.send(struct.pack("I", len(message)))
s.send(message)
print(s.recv(32).decode('utf-8'))   #receive 'ok' to confirm connection with bot_data information

#--------AI---------
def move(JEF_towerPosition : list, JEF_currentInStateJson : int, forward : bool, Rdiagonal:bool, Ldiagonal : bool) -> list:
    currentPosition = [JEF_towerPositionLine, JEF_towerPositionColomn]
    dx = random.randint(0,7)
    dy = random.randint(0,7)
    if JEF_currentInStateJson == 0:
        if forward:
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]]
        if Rdiagonal:
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]+random.randint(0,currentPosition[1])]
        if Ldiagonal:
            finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]-random.randint(0,currentPosition[1])]

    elif JEF_currentInStateJson == 1:
        if forward:
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]]
        if Rdiagonal:
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]-random.randint(0,7-currentPosition[1])]
        if Ldiagonal:
            finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]+random.randint(0,7-currentPosition[1])]

    return [currentPosition, finalPosition]





#-------------listen ping and answer pong in TCP-------------
#(desactiver les deux pare-feux windows defender dans pare-feux windows defender pour recevoir les messages)
pps = socket.socket()
pps.bind(myAdress)
pps.listen()
pps.settimeout(0.5)

while True:
    try:
        client, address = pps.accept()
        with client:
            len_info = client.recv(4)
            len_mes = struct.unpack("I", len_info)[0] #4byte en int de tuple(int,) où on prand le 1er
            client_message = client.recv(len_mes).decode('utf-8')  #receive ping

            print(client_message)
            if "ping" in client_message:
                pong_data = {
                    "response": "pong"
                }
                pong_message = json.dumps(pong_data).encode('utf-8')
                client.send(struct.pack("I", len(pong_message)))
                client.send(pong_message)   #send pong
                print(pong_data)
            if "play" in client_message:
                print(client_message)
            
    except socket.timeout:
        pass


