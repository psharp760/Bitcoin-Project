# Program: Bitcoin Socket Project
# Authors: Peter Sharp, Hieu Nguyen, Daniel Martinez 
# Class: CS 436

# clientA_receive.py

from socket import *
import os

clientPortA = 15001
clientSocketA = socket(AF_INET, SOCK_DGRAM)
clientSocketA.bind(('', clientPortA))
print('client A is ready to receive.\n')

while 1:
	message, serverAddress = clientSocketA.recvfrom(2048)
	modifiedMessage = message.decode()

	if (modifiedMessage == 'true'):
		print('full node 1 has sent a message.\n')
		with open('unconfirmed_TA.txt', 'r') as unconfirmed:
			lines = unconfirmed.read()
		with open('confirmed_TA.txt', 'a') as confirmed:
			confirmed.write(lines)
		unconfirmed.close()

		n = 4
		nfirstlines = []

		with open("temp_TA.txt","r") as f, open("temp_t2A.txt", "w") as out:
			for x in range(n):
				nfirstlines.append(next(f))
			for line in f:
				out.write(line)

		with open("unconfirmed_TA.txt","r") as f2, open("unconfirmed2A.txt", "w") as out1:
			for x in range(n):
				nfirstlines.append(next(f2))
			for line in f2:
				out1.write(line)

		os.remove("temp_TA.txt")
		os.rename("temp_t2A.txt", "temp_TA.txt")
		os.remove("unconfirmed_TA.txt")
		os.rename("unconfirmed2A.txt", "unconfirmed_TA.txt")

	else:
		tempBalFile = open('tempBalA.txt', 'w')
		tempBalFile.write(modifiedMessage)
		# print(modifiedMessage)
		tempBalFile.close()

