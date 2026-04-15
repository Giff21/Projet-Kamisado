import socket
import json
import struct

def send_json(s,data: dict) -> None:  #https://oneuptime.com/blog/post/2026-03-20-json-over-ipv4-sockets-python/view
    """Serialize data to JSON and send with a 4-byte length prefix."""
    message = json.dumps(data).encode("utf-8")
    # Pack the length as a 4-byte big-endian unsigned integer
    header = struct.pack("<I", len(message))
    s.send(header + message)

def recv_json(sock: socket.socket) -> dict:
    """Receive a length-prefixed JSON message from the socket."""
    # Read exactly 4 bytes for the length header
    raw_len = recvn(sock,4)

    if not raw_len:
        raise ConnectionError("Connection closed while reading header")
    
    msg_len = struct.unpack("<I", raw_len)[0] # "<I" = Little-endian

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

        if not chunk:
            return b""
        buf += chunk
    return buf

def inscription(s):
    inscription_Json ={
        "request": "subscribe",
        "port": 8888,
        "name": "U+1F624",
        "matricules": ["24087", "24092"]
    }
    send_json(s,inscription_Json)
    print("insciption sent")

def pingRequest(clientSock):
    pong ={
    "response": "pong"
    }
    send_json(clientSock,pong)
    print('ping sent')

#############################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls = socket.socket()
ls.bind(("0.0.0.0",8888))

try:
    address = ('172.20.10.2', 3000) # 172.17.10.41 addr serv lur port 3000  par défaut
    s.connect(address) 
    print(f"connected to {address}")
except OSError :
    print ("Serveur introuvable , connexion impossible .")

inscription(s)
print(recv_json(s))

ls.settimeout(2)
ls.listen()
while True:
    try: 
        client, adress = ls.accept()
        with client:
            recu =recv_json(client)
            print(recu)
            if recu['request'] == "ping":  #ERROR I just want the word ping 
                print("PING")
                pingRequest(client)
                print("PONG")
    except socket.timeout:
        pass