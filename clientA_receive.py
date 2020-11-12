# clientA_receive.py
from socket import *

serverName = 'localhost'
serverPort2 = 54321
clientSocket2 = socket(AF_INET, SOCK_DGRAM)

message, serverAddress = clientSocket2.recvfrom(2048)
modifiedMessage = message.decode()

print(modifiedMessage)