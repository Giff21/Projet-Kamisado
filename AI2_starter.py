from communication import inscription, server_communication

serverIP = "192.168.129.11"
clientPort = 8889
smart = False

if __name__ == "__main__":
    inscription("Hello2", [33333, 44444], serverIP, clientPort)
    server_communication(clientPort, smart)
