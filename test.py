import socket
import struct
import json

# envoyer une message en TCP
s = socket.socket()
serverAddress = ('172.17.10.41', 3000)
s.connect(serverAddress)

Dict ={
  "request": "subscribe",
  "port": 8888,
  "name": "Florian",
  "matricules": ["24092", "67890"]
}

message = json.dumps(Dict).encode()
s.send(struct.pack("I", len(message)))
s.send(message)
print(s.recv(2048))

