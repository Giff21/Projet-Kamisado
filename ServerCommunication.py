import socket
import struct
import json

# send the connection message in TCP
serverAddress = ('10.28.157.176', 3000)  #ip and port of teacher
myAdress = ('0.0.0.0', 8888)    #my IP and listening port

bot_data ={
    "request": "subscribe",
    "port": 8888,
    "name": "SexyWizard",
    "matricules": ["24092", "24087"]
}

s = socket.socket()
s.connect(serverAddress)
message = json.dumps(bot_data).encode('utf-8')
s.send(struct.pack("I", len(message)))
s.send(message)
print(s.recv(32).decode('utf-8'))   #receive 'ok' to confirm connection with bot_data information

#listen ping and answer pong in TCP
#(desactiver les deux pare-feux windows defender dans pare-feux windows defender pour recevoir les messages)
pps = socket.socket()
pps.bind(myAdress)
pps.listen()
pps.settimeout(0.5)

while True:
    try:
        client, address = pps.accept()
        with client:
            ping_message = client.recv(32).decode('utf-8')  #receive ping
            print(ping_message)
            if "ping" in ping_message:
                pong_data = {
                    "response": "pong"
                }
                pong_message = json.dumps(pong_data).encode('utf-8')
                client.send(struct.pack("I", len(pong_message)))
                client.send(pong_message)   #send pong
                print(pong_data)
    except socket.timeout:
        pass


