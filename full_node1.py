# full_node1.py
from socket import *

# socket for receiving from clientA_send.py
serverPort1 = 12345
serverSocket1 = socket(AF_INET, SOCK_DGRAM)

# socket for sending to clientA_receive.py
serverPort2 = 54321
serverSocket2 = socket(AF_INET, SOCK_DGRAM)

serverSocket1.bind(('', serverPort1))
print('full_node1 is ready to receive.\n')

serverSocket2.bind(('', serverPort2))
print('full_node1 is ready to send.\n')

# open temp_T.txt to write 
fileTxTemp = open('temp_T.txt', 'w+')

txFee = 2
miningFee = 30 
fullNodeBalance = 0
txCount = 0
blockChain = []

while 1: 
	message, clientAddress = serverSocket1.recvfrom(2048)
	tx = message.decode()
	# append tx to temp_T.txt
	fileTxTemp.write(str(tx) + '\n')
	txCount += 1
	blockChain.append(tx)

	fileBlockChain = open('blockchain.txt', 'w')

	if (len(blockChain) % 4 == 0):
		fullNodeBalance = ((txFee * 4)+ miningFee)
		for line in blockChain:
			fileBlockChain.write(''.join(line) + '')


		# 1 2 3 4 5 6 7 8 ...
		# 1234 5678 ...

	# create temp tx array to store each tx
	# if temp tx array length % 4 == 0 
		# write to blockchain array
		# write to blockchain.txt
		# remove temp_tx array
		# remove from temp_T.txt 

		


	
# serverSocket2.sendto(modifiedMessage.encode(), clientAddress)


