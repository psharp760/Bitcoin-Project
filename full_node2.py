# full_node2.py
from socket import *

# socket for receiving from clientB_send.py
serverPortB = 20000
serverSocketB = socket(AF_INET, SOCK_DGRAM)
serverSocketB.bind(('', serverPortB))
print('full node 2 is ready to receive.\n')

# sending to clientB_receive.py
clientName = 'localhost'
clientPortB = 20001
clientSocketB = socket(AF_INET, SOCK_DGRAM)

# socket for receiving from full_node1.py
clientPortA = 20002
clientSocketA = socket(AF_INET, SOCK_DGRAM)
clientSocketA.bind(('', clientPortA))

# sending to full_node1.py
serverName = 'localhost'
serverPortA = 15002
serverSocketA = socket(AF_INET, SOCK_DGRAM)


txFee = 2
miningFee = 30
fullNodeBalance = 0
blockChain = []
serverHeader = 'F'

while 1:
    message, clientAddress = serverSocketB.recvfrom(2048)
    tx = message.decode()
    
    if (tx[0] == 'C'):
        tx = tx[1:]
        blockChain.append(tx)

        txF1 = str.encode(str(serverHeader + tx), 'utf-8')
        serverSocketA.sendto(txF1, (serverName, serverPortA))

        message1, f1Address = clientSocketA.recvfrom(2048)
        txFromF1 = message1.decode()
        
        if (txFromF1[0] == 'F'):
            txFromF1 = txFromF1[1:]
            clientSocketB.sendto(txFromF1.encode(), (clientName, clientPortB))
            # print(txFromF1)

        with open('temp_TB.txt', 'w') as fileTxTemp:
            i = 0
            while i < len(blockChain):
                line = blockChain[i] + '\n'
                fileTxTemp.write(line)
                i += 1

        if (len(blockChain) % 4 == 0):
            fullNodeBalance = ((txFee * 4) + miningFee)

            with open('blockchain.txt', 'a') as fileBlockChain:
                i = 0
                while i < len(blockChain):
                    block = blockChain[i] + blockChain[i + 1] + blockChain[i + 2] + blockChain[i + 3] + '\n'
                    fileBlockChain.write(block)
                    i += 4
                fileBlockChain.close()
            messageToB = 'true'
            clientSocketB.sendto(messageToB.encode(), (clientName, clientPortB))





