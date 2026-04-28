from communication import inscription, server_communication

serverIP = "192.168.129.11"
clientPort = 8888
smart = False
time_limit = 2.5  # max 3s

if __name__ == "__main__":
    inscription("Hello", [11111, 22222], serverIP, clientPort)
    server_communication(clientPort, smart, time_limit)
