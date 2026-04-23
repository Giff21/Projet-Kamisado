from communication import inscription, serverCom

serverIP = "172.17.10.54"
clientPort = 8889

if __name__ == "__main__":
    inscription("Hello2", [33333,44444], serverIP, clientPort)
    serverCom(clientPort)