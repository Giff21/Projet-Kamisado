from src.communication import inscription, server_communication

serverIP = "192.168.129.11"
clientPort = 8888
smart = True
time_limit = 2.5  # max 3s

if __name__ == "__main__":
    inscription("Wizard-of-OZ", [24087, 24092], serverIP, clientPort)
    server_communication(clientPort, smart, time_limit)
