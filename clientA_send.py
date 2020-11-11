# clientA_send.py
from socket import *

def menu():
	
	print('1.	Enter new transaction\n')
	print('2.	Display current balance of each account\n')
	print('3. 	Display unconfirmed transactions\n')
	print('4. 	Display last X number of confirmed transactions\n')
	print('5. 	Display Blockchain\n')
	print('6. 	Exit program\n')		

def main():

	serverName = 'localhost'
	serverPort = 12345
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	unconfirmedBalanceA1 = 1000
	confirmedBalanceA1 = 1000
	unconfirmedBalanceA2 = 1000
	confirmedBalanceA2 = 1000

	txFee = 2

	fileUnconfirmedTx = open('unconfirmed_T.txt', 'w')
	# fileBalance = open('balance.txt', 'w')

	clientSocket.connect((serverName, serverPort))

	loop = True
	while loop:
		menu()
		option = input('Input choice (1 - 6): ')

		if (option == '1'):
			print('Option 1 has been selected.\n')
			print('Select the Payer:\n')
			print('1.\tA0000001\n')
			print('2.\tA0000002\n')
			payerInput = input('Choice: ')
			print('Select the Payee:\n')
			print('1.\tB0000001\n')
			print('2.\tB0000002\n')
			payeeInput = input('Choice: ')
			amountInput = input ('Input the amount of payment in decimal:\n')
			txAmount = int(amountInput)

			if (payerInput == '1'):
				payer = 'A0000001'
				unconfirmedBalance = unconfirmedBalanceA1	
			elif (payerInput == '2'):
				payer = 'A0000002'
				unconfirmedBalance = unconfirmedBalanceA2
			if (payeeInput == '1'):
				payee = 'B0000001'	
			elif (payeeInput == '2'):
				payee = 'B0000002'

			if (txAmount + txFee > unconfirmedBalance):
				print("ERROR: Cannot process transaction. Insufficent funds.\n")
			elif (txAmount + txFee <= unconfirmedBalance):
				print('Tx: ' + payer + ' pays ' + payee + ' the amount of ' + str(txAmount) + ' BC.\n')
				tx = (payer + payee + hex(txAmount))
				unconfirmedBalance -= (txAmount + txFee)
				fileUnconfirmedTx.write(str(tx) + '\n')
				# send tx to server
				# update balance.txt with ne unconfirmed balance 
			
		elif(option == '2'):
			print('Option 2 has been selected.\n')
		elif(option == '3'):
			print('Option 3 has been selected.\n')
		elif(option == '4'):
			print('Option 4 has been selected.\n')
		elif(option == '5'):
			print('Option 5 has been selected.\n')
		elif(option == '6'):
			print('Program has been quit.\n')
			loop = False
		else:
			input('ERROR: input selection invalid. Input any key to try again.\n')

	fileUnconfirmedTx.close()
	# fileBalance.close()
	clientSocket.close()

main()

	# message = str.encode(str(option), 'utf-8')
	# clientSocket.send(message)
	# print(clientSocket.recvfrom(2048))
	# option = input()
	# message = str.encode(str(option), 'utf-8')
	# clientSocket.sendto(message)
	# print(str(clientSocket.recvfrom(2048)))

# clientSocket.sendto(userInput.encode(), (serverName, serverPort))

# modifiedInput, serverAddress = clientSocket.recvfrom(2048)

# print(modifiedInput.decode())


