import socket
import json



with open("dict.json","rw") as file:
    content = json.loads("file")
with open("dict.json","w") as file:
         json.dumps

s = socket.socket()
address = ("172.17.10.41", 3000)
s.connect(address) 
if s.connect(address) == True:
    print("Connected")
msg = input("msg : ", )
sent = msg.encode("utf-8")
s.send(sent)