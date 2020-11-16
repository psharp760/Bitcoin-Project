# full_node1.py
from socket import *

# socket for receiving from clientA_send.py
serverPortA = 15000
serverSocketA = socket(AF_INET, SOCK_DGRAM)
serverSocketA.bind(('', serverPortA))
print('full node 1 is ready to receive.\n')

#sending to clientA_receive.py
clientName = 'localhost'
clientPortA = 15001
clientSocketA = socket(AF_INET, SOCK_DGRAM)

txFee = 2
miningFee = 30 
fullNodeBalance = 0
blockChain = []

while 1: 
	message, clientAddress = serverSocketA.recvfrom(2048)
	tx = message.decode()
	blockChain.append(tx)

	with open('temp_TA.txt', 'w') as fileTxTemp:
		i = 0
		while i < len(blockChain):
			line = blockChain[i] + '\n'
			fileTxTemp.write(line)
			i += 1

	if (len(blockChain) % 4 == 0):
		fullNodeBalance = ((txFee * 4)+ miningFee)

		with open('blockchainA.txt', 'w') as fileBlockChain:
			i = 0
			while i < len(blockChain):
				block = blockChain[i] + blockChain[i + 1] + blockChain[i + 2] + blockChain[i + 3] + '\n'
				fileBlockChain.write(block)
				i += 4

		messageToA = 'true'
		clientSocketA.sendto(messageToA.encode(), (clientName, clientPortA))




