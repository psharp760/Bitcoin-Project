# clientA_send.py
from socket import *

def menu():
	print('1.	Enter new transaction\n')
	print('2.	Display current balance of each account\n')
	print('3. 	Display unconfirmed transactions\n')
	print('4. 	Display last X number of confirmed transactions\n')
	print('5. 	Display Blockchain\n')
	print('6. 	Exit program\n')



serverName = 'localhost'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.connect((serverName, serverPort))

while True:
	menu()
	print('Input choice: ')
	option = input()
	message = str.encode(str(option), 'utf-8')
	clientSocket.send(message)
	print(clientSocket.recvfrom(2048))
	option = input()
	message = str.encode(str(option), 'utf-8')
	clientSocket.sendto(message)
	print(str(clientSocket.recvfrom(2048)))

clientSocket.close()

# clientSocket.sendto(userInput.encode(), (serverName, serverPort))

# modifiedInput, serverAddress = clientSocket.recvfrom(2048)

# print(modifiedInput.decode())
