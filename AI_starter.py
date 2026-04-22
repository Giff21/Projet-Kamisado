from communication import inscription, serverCom

serverIP = "192.168.1.27"

if __name__ == "__main__":
    inscription("Hello", [11111,22222], serverIP)
    serverCom()


