import socket
import struct
import json

# send the connection message in TCP
serverAddress = ('172.17.10.41', 3000)  #ip and port of teacher
myAdress = ('0.0.0.0', 8888)    #my IP and listening port

bot_data ={
  "request": "subscribe",
  "port": 8888,
  "name": "SexyWizard",
  "matricules": ["24092", "24087"]
}

s = socket.socket()
s.connect(serverAddress)
message = json.dumps(bot_data).encode()
s.send(struct.pack("I", len(message)))
s.send(message)
print(s.recv(2).decode())   #receive 'ok' to confirm connection with bot_data information

#listen ping and answer pong in TCP
#(desactiver les deux perfeux windows defender dans pare-feu windows defender pour recevoir les messages)
pps = socket.socket()
pps.bind(myAdress)
pps.listen()
pps.settimeout(0.5)

while True:
    try:
        client, address = pps.accept()
        with client:
            ping_message = client.recv(4).decode()  #receive ping
            print(ping_message)
            if ping_message == "ping":
                pong_data = {
                      "response": "pong"
                }
                pong_message = json.dumps(pong_data).encode()
                client.send(struct.pack("I", len(pong_message)))
                client.send(pong_message)   #send pong
    except socket.timeout:
        pass


