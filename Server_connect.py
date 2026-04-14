import socket
import json
import struct

def send_json( data: dict) -> None:  #https://oneuptime.com/blog/post/2026-03-20-json-over-ipv4-sockets-python/view
    """Serialize data to JSON and send with a 4-byte length prefix."""
    message = json.dumps(data).encode("utf-8")
    # Pack the length as a 4-byte big-endian unsigned integer
    header = struct.pack("<I", len(message))
    s.send(header + message)

def recv_json(sock: socket.socket) -> dict:
    """Receive a length-prefixed JSON message from the socket."""
    # Read exactly 4 bytes for the length header
    raw_len = recvn(sock,4)
#    print("HEADER RAW:", raw_len)

    if not raw_len:
        raise ConnectionError("Connection closed while reading header")
    
    msg_len = struct.unpack("<I", raw_len)[0] # "<I" = Little-endian
#    print("LONGUEUR ATTENDUE:", msg_len)

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
#        print("RECU:", chunk)
        if not chunk:
            return b""
        buf += chunk
    return buf

def inscription():
    inscription_Json ={
        "request": "subscribe",
        "port": 8888,
        "name": "U+1F624",
        "matricules": ["24087", "24092"]
    }
    send_json(inscription_Json)
    print("insciption sent")
    # message = json.dumps(inscription_Json).encode()
    # s.send(struct.pack("I", len(message)))
    # s.send(message)
    # print("sent inscription request")

def pingRequest():
    pong ={
        "response": "pong"
    }
    message = json.dumps(pong).encode()
    s.send(struct.pack("I", len(message)))
    s.send(message)

#############################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    address = ('10.0.0.144', 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
    print(f"connected to {address}")
except OSError :
    print ("Serveur introuvable , connexion impossible .")

inscription()
recv_json(s)


# Décodage et traitement du JSON
ls = socket.socket()
ls.bind(("localhost",8888))
ls.settimeout(0.5)
while True:
    try: 
        client, adress = ls.accept()
        with client:
            message = client.recv()
            message.decode()
            print(message)      #recieve ping in json (ok)
            #if ping then send pong message in json
            if json.loads(message['reponse']) == "ping":  #ERROR I just want the word ping 
                pingRequest()
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
