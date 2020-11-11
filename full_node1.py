# full_node1.py
from socket import *
import sys

class Account():

	def __init__(self):
		# read her prompt, we need to have confirmed and unconfirmed balance
		# confirmed and unconfirmed transaction, we need to read and write to files









serverPort = 12345
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print('full_node1 is ready to receive.')

while 1: 
	userInput, clientAddress = serverSocket.recvfrom(2048)
	
	modifiedInput = userInput.decode()
	if (modifiedInput == 1):
		print('hi')



	# serverSocket.sendto(modifiedInput.encode(), clientAddress)


