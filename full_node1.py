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

fullNodeBalance = 0
txCount = 0

while 1: 
	message, clientAddress = serverSocket1.recvfrom(2048)
	tx = message.decode()
	# append tx to temp_T.txt
	fileTxTemp.write(str(tx) + '\n')
	txCount += 1
	txn = fileTxTemp.read()

	print(txn)
	
	# if (txCount % 4 == 0):
		



	# add to blockchain
	# send 
	
# serverSocket2.sendto(modifiedMessage.encode(), clientAddress)


