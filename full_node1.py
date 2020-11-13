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

# open temp_T.txt to write 
fileTxTemp = open('temp_T.txt', 'w+')

txFee = 2
miningFee = 30 
fullNodeBalance = 0
txCount = 0
blockChain = []

while 1: 
	message, clientAddress = serverSocketA.recvfrom(2048)
	tx = message.decode()
	# append tx to temp_T.txt
	fileTxTemp.write(str(tx) + '\n')
	blockChain.append(tx)
	txCount += 1

	fileBlockChain = open('blockchain.txt', 'w')

	if (len(blockChain) % 4 == 0):
		fullNodeBalance = ((txFee * 4)+ miningFee)
		for line in blockChain:
			fileBlockChain.write(''.join(line) + '')

		messageToA = 'Test message to client A.\n'
		clientSocketA.sendto(messageToA.encode(), (clientName, clientPortA))




		# 1 2 3 4 5 6 7 8 ...
		# 1234 5678 ...

	# create temp tx array to store each tx
	# if temp tx array length % 4 == 0 
		# write to blockchain array
		# write to blockchain.txt
		# remove temp_tx array
		# remove from temp_T.txt 

		


	
# serverSocket2.sendto(modifiedMessage.encode(), clientAddress)


