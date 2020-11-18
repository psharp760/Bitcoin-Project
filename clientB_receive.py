# Program: Bitcoin Socket Project
# Authors: Peter Sharp, Hieu Nguyen, Daniel Martinez 
# Class: CS 436

# clientB_receive.py

from socket import *
import os

clientPortB = 20001
clientSocketB = socket(AF_INET, SOCK_DGRAM)
clientSocketB.bind(('', clientPortB))
print('client B is ready to receive.\n')

while 1:
	message, serverAddress = clientSocketB.recvfrom(2048)
	modifiedMessage = message.decode()

	if (modifiedMessage == 'true'):
		print('full node 1 has sent a message.\n')
		with open('unconfirmed_TB.txt', 'r') as unconfirmed:
			lines = unconfirmed.read()
		with open('confirmed_TB.txt', 'a') as confirmed:
			confirmed.write(lines)
		unconfirmed.close()

		n = 4
		nfirstlines = []

		with open("temp_TB.txt","r") as f, open("temp_t2B.txt", "w") as out:
			for x in range(n):
				nfirstlines.append(next(f))
			for line in f:
				out.write(line)

		with open("unconfirmed_TB.txt","r") as f2, open("unconfirmed2B.txt", "w") as out1:
			for x in range(n):
				nfirstlines.append(next(f2))
			for line in f2:
				out1.write(line)

		os.remove("temp_TB.txt")
		os.rename("temp_t2B.txt", "temp_TB.txt")
		os.remove("unconfirmed_TB.txt")
		os.rename("unconfirmed2B.txt", "unconfirmed_TB.txt")

	else:
		tempBalFile = open('tempBalB.txt', 'w')
		tempBalFile.write(modifiedMessage)
		# print(modifiedMessage)
		tempBalFile.close()

