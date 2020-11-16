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
		with open('unconfirmed_T.txt', 'r') as unconfirmed:
			lines = unconfirmed.read()
		with open('confirmed_T.txt', 'a') as confirmed:
			confirmed.write(lines)
		unconfirmed.close()

		n = 4
		nfirstlines = []

		with open("temp_T.txt","r") as f, open("temp_t2.txt", "w") as out:
			for x in range(n):
				nfirstlines.append(next(f))
			for line in f:
				out.write(line)

		with open("unconfirmed_T.txt","r") as f2, open("unconfirmed2.txt", "w") as out1:
			for x in range(n):
				nfirstlines.append(next(f2))
			for line in f2:
				out1.write(line)

		os.remove("temp_T.txt")
		os.rename("temp_t2.txt", "temp_T.txt")
		os.remove("unconfirmed_T.txt")
		os.rename("unconfirmed2.txt", "unconfirmed_T.txt")
