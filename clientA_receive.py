# clientA_receive.py
from socket import *

clientPortA = 15001
clientSocketA = socket(AF_INET, SOCK_DGRAM)
clientSocketA.bind(('', clientPortA))
print('client A is ready to receive.\n')

while 1:
	message, serverAddress = clientSocketA.recvfrom(2048)
	print('full node 1 has sent a message.\n')
	modifiedMessage = message.decode()
	print(modifiedMessage)