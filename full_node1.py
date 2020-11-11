# full_node1.py
from socket import *

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print('full_node1 is ready to receive.')

while 1: 
	userInput, clientAddress = serverSocket.recvfrom(2048)
	
	modifiedInput = userInput.decode()



	# serverSocket.sendto(modifiedInput.encode(), clientAddress)


