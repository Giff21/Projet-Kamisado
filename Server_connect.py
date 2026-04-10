import socket
import json
import struct

def send_json(s, data: dict) -> None:  #https://oneuptime.com/blog/post/2026-03-20-json-over-ipv4-sockets-python/view
    """Serialize data to JSON and send with a 4-byte length prefix."""
    payload = json.dumps(data).encode("utf-8")
    # Pack the length as a 4-byte big-endian unsigned integer
    header = struct.pack(">I", len(payload))
    s.sendall(header + payload)

def inscription():
    inscription_Json ={
        "request": "subscribe",
        "port": 8888,
        "name": "U+1F624",
        "matricules": ["24087", "24092"]
    }
    send_json(address,inscription_Json)
    # message = json.dumps(inscription_Json).encode()
    # s.send(struct.pack("I", len(message)))
    # s.send(message)
    # print("sent inscription request")

def pingRequest(message):
    pong ={
        "response": "pong"
    }
    message = json.dumps(pong).encode()
    s.send(struct.pack("I", len(message)))
    s.send(message)

s = socket.socket()
ls = socket.socket()
ls.bind(("localhost",8888))
try:
    address = ("172.17.83.69", 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
    print("connected")
except OSError :
    print ("Serveur introuvable , connexion impossible .")

inscription()
# Décodage et traitement du JSON
data = s.recv(64)
try:
    json_data = json.loads(data.decode())
    print("Données JSON reçues :", json_data )#["response"])
except json.JSONDecodeError:
    print("Erreur de décodage JSON")

ls.settimeout(0.5)
while True:
    try: 
        client, adress = ls.accept()
        with client:
            message = client.recv()
            message.decode()
            print(message)      #recieve ping in json (ok)
            #if ping then send pong message in json
            if json.loads(message) == "ping":  #ERROR I just want the word ping 
                pingRequest(message)
    except socket.timeout:
        pass



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
