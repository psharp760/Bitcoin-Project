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

# socket for receiving from full_node2.py
clientPortB = 15002
clientSocketB = socket(AF_INET, SOCK_DGRAM)
clientSocketB.bind(('', clientPortB))

# sending to full_node2.py
serverName = 'localhost'
serverPortB = 20002
serverSocketB = socket(AF_INET, SOCK_DGRAM)

txFee = 2
miningFee = 30 
fullNodeBalance = 0
blockChain = []
serverHeader = 'F'

while 1: 
	message, clientAddress = serverSocketA.recvfrom(2048)
	tx = message.decode()

	if (tx [0] == 'C'):
		tx = tx[1:]
		blockChain.append(tx)

		txF2 = str.encode(str(serverHeader + tx), 'utf-8')
		serverSocketB.sendto(txF2, (serverName, serverPortB))

		message1, f2Address = clientSocketB.recvfrom(2048)
		txFromF2 = message1.decode()

		if (txFromF2[0] == 'F'):
			txFromF2 = txFromF2[1:]
			clientSocketA.sendto(txFromF2.encode(), (clientName, clientPortA))
			# print(txFromF2)

		with open('temp_TA.txt', 'w') as fileTxTemp:
			i = 0
			while i < len(blockChain):
				line = blockChain[i] + '\n'
				fileTxTemp.write(line)
				i += 1

		if (len(blockChain) % 4 == 0):
			fullNodeBalance = ((txFee * 4)+ miningFee)

			with open('blockchain.txt', 'a') as fileBlockChain:
				i = 0
				while i < len(blockChain):
					block = blockChain[i] + blockChain[i + 1] + blockChain[i + 2] + blockChain[i + 3] + '\n'
					fileBlockChain.write(block)
					i += 4
			blockChain.clear()		
			messageToA = 'true'
			clientSocketA.sendto(messageToA.encode(), (clientName, clientPortA))




