from communication import inscription, serverCom

serverIP = "172.17.10.54"
clientPort = 8888

if __name__ == "__main__":
    inscription("Hello", [11111,22222], serverIP, clientPort)
    serverCom(clientPort)


