# full_node2.py
from socket import *

# socket for receiving from clientA_send.py
serverPortB = 20000
serverSocketB = socket(AF_INET, SOCK_DGRAM)
serverSocketB.bind(('', serverPortB))
print('full node 2 is ready to receive.\n')

# sending to clientA_receive.py
clientName = 'localhost'
clientPortB = 20001
clientSocketB = socket(AF_INET, SOCK_DGRAM)

txFee = 2
miningFee = 30
fullNodeBalance = 0
blockChain = []

while 1:
    message, clientAddress = serverSocketB.recvfrom(2048)
    tx = message.decode()
    blockChain.append(tx)

    with open('temp_T.txt', 'w') as fileTxTemp:
        i = 0
        while i < len(blockChain):
            line = blockChain[i] + '\n'
            fileTxTemp.write(line)
            i += 1

    if (len(blockChain) % 4 == 0):
        fullNodeBalance = ((txFee * 4) + miningFee)

        with open('blockchain.txt', 'w') as fileBlockChain:
            i = 0
            while i < len(blockChain):
                line = blockChain[i] + blockChain[i + 1] + blockChain[i + 2] + blockChain[i + 3] + '\n'
                fileBlockChain.write(line)
                i += 4

        messageToB = 'true'
        clientSocketB.sendto(messageToB.encode(), (clientName, clientPortB))
