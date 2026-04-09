import socket

s = socket.socket()
address = ("172.17.10.41", 5000)
s.connect(address) 
if s.connect(address) == True:
    print("Connected")
msg = input("msg : ", )
sent = msg.encode("utf-8")
s.send(sent)