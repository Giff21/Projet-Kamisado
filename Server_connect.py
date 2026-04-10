import socket
import json
import struct

# with open("dict.json","r") as file:
#     content = json.loads("file")
# with open("dict.json","w") as file:
#          json.dumps

def inscription():
    inscription_Json ={
        "request": "subscribe",
        "port": 8888,
        "name": "U+1F624",
        "matricules": ["12345", "67890"]
    }
    message = json.dumps(inscription_Json).encode()
    s.send(struct.pack("I", len(message)))
    s.send(message)


def pingRequest():
     ping ={
        "response": "pong"
    }

s = socket.socket()
try:
    address = ("172.17.83.69", 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
except OSError :
    print ("Serveur introuvable , connexion impossible .")


inscription()
# ls = socket.socket()
# ls.bind(("localhost",8888))

# print (ls. getsockname () )

# ls.listen(8888)
# ls.accept()
# chunks = []
# finished = False
# while not finished :
#     data = ls.recv (2048)
#     chunks . append ( data )
#     finished = data == b""
#     print (b"". join ( chunks ). decode () )
#     print (data.decode())
# print(s.recv(2048))



# def _compute (self) :
#     totalsent = 0
#     msg = pickle.dumps ( self . __data )
#     self . __s . send ( struct.pack ("I", len ( msg )))
#     while totalsent < len ( msg ):
#         sent = self . __s . send ( msg [ totalsent :])
#         totalsent += sent
#     return struct.unpack ("I", self . __s . recv (4) ) [0]

# chunks = []
# finished = False
# while not finished :
#     data = client.recv (1024)
#     chunks . append ( data )
#     finished = data == b""
#     print (b"". join ( chunks ) . decode () )

# s.listen()
# while True:
#     packet = address.recv(1024)
#     if not packet: break
#     data += packet
            
# # Décodage et traitement du JSON
# try:
#     json_data = json.loads(data.decode('utf-8'))
#     print("Données JSON reçues :", json_data)
#     # Exemple d'accès : print(json_data['cle'])
# except json.JSONDecodeError:
#     print("Erreur de décodage JSON")
