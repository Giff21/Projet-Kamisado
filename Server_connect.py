import socket
import json



with open("dict.json","rw") as file:
    content = json.loads("file")
with open("dict.json","w") as file:
         json.dumps

s = socket.socket()
address = ("172.17.10.41", 3000) #port 3000  par défaut
s.connect(address) 
if s.connect(address) == True:
    print("Connected")

s.listen()
while True:
    packet = address.recv(1024)
    if not packet: break
    data += packet
            
# Décodage et traitement du JSON
try:
    json_data = json.loads(data.decode('utf-8'))
    print("Données JSON reçues :", json_data)
    # Exemple d'accès : print(json_data['cle'])
except json.JSONDecodeError:
    print("Erreur de décodage JSON")

def inscription():
    inscription_Json ={
        "request": "subscribe",
        "port": 8888,
        "name": "fun_name_for_the_client",
        "matricules": ["12345", "67890"]
    }
def pingRequest():
     ping ={
        "response": "pong"
    }
msg = input("msg : ", )
sent = msg.encode("utf-8")
s.send(sent)