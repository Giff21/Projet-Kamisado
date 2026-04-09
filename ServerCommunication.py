import socket
import struct
import json

# send the connection message in TCP
s = socket.socket()
serverAddress = ('172.17.10.41', 3000)  #ip and port of teacher
s.connect(serverAddress)

Dict ={
  "request": "subscribe",
  "port": 8888,
  "name": "SexyWizard",
  "matricules": ["24092", "24087"]
}

message = json.dumps(Dict).encode()
s.send(struct.pack("I", len(message)))
s.send(message)
print(s.recv(32))

#listen ping and answer pong in TCP
ls = socket.socket()
myAdress = ('0.0.0.0', 8888)        #my IP and listening port
ls.bind(myAdress)
ls.settimeout(0.5)
ls.listen()

#desactiver les deux perfeux windows defender dans pare-feu windows defender pour recevoir les messages
while True:
    try: 
        client, adress = ls.accept()
        with client:
            message = client.recv(4)
            message.decode()
            print(message)      #recieve ping in json (ok)
            #if ping then send pong message in json
            if json.loads(message) == "ping":  #ERROR I just want the word ping 
                pong = {
                      "response": "pong"
                }
                message = json.dumps(pong).encode()
                s.send(struct.pack("I", len(message)))
                s.send(message)
    except socket.timeout:
        pass


