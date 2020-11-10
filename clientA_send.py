# clientA_send.py
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def printMenu ():
	
	print('Client Menu\n')
	print('1.	Enter new transaction\n')
	print('2.	Display current balance of each account\n')
	print('3.	Display unconfirmed transactions\n')
	print('4.	Display last X number of confirmed transactions\n')
	print('5.	Display Blockchain\n')
	print('6.	Exit program\n')

def mainMenu ():
	
	loop = True
	while loop:
		printMenu()
		choice = input("Enter your choice [1 - 6]:\n")
		choice = int(choice)

		if (choice == 1):
			print('Option 1 has been selected.\n')
			transaction ()
		elif (choice == 2):
			print('Option 2 has been selected.\n')
		elif (choice == 3):
			print('Option 3 has been selected.\n')
		elif (choice == 4):
			print('Option 4 has been selected.\n')
		elif (choice == 5):
			print('Option 5 has been selected.\n')
		elif (choice == 6):
			print('Quitting program.\n')
			loop = False
		else:
			input('ERROR: Incorrect menu option. Input any key to try again.\n')

def transaction ():

	print('Select the Payer:\n')
	print('1.	A0000001\n')
	print('2.	A0000002\n')
	payerChoice = input('Choice:\n')
	print('Select the Payee:\n')
	print('1.	B0000001\n')
	print('2.	B0000002\n')
	payeeChoice = input('Choice:\n')
	amountChoice = input('Input the amount of payment in decimal.\n')
	



mainMenu()

