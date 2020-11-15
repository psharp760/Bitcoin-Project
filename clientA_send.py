# clientA_send.py
from socket import *

# menu() function displays menu to user
def menu():
	
	print('1.	Enter new transaction\n')
	print('2.	Display current balance of each account\n')
	print('3. 	Display unconfirmed transactions\n')
	print('4. 	Display last X number of confirmed transactions\n')
	print('5. 	Display Blockchain\n')
	print('6. 	Exit program\n')	
# end of menu()

# main() function driver program for clientA_send
def main():

	serverName = 'localhost'                            # establish connection to server
	serverPortA = 15000                                 # set port number
	clientSocketA = socket(AF_INET, SOCK_DGRAM)         # create socket
	clientSocketA.connect((serverName, serverPortA))    # connect socket to server

	unconfirmedBalanceA1 = 1000     # unconfirmed balance for account A0000001
	confirmedBalanceA1 = 1000       # confirmed balance for account A0000001
	unconfirmedBalanceA2 = 1000     # unconfirmed balance for account A0000002
	confirmedBalanceA2 = 1000       # confirmed balance for account A0000002
	txFee = 2                       # transaction fee 

	loop = True     # bool variable loop initialized to True
	while loop:     # while 'loop' is true loop through contents below
		menu()      # call menu() function to display menu
		option = input('Input choice (1 - 6): ')        # get user input for menu(), store in option		

		if (option == '1'):                             # check if user inputs option 1 to enter new transaction
			print('Option 1 has been selected.\n')      # print sub menu for user to input transaction
			print('Select the Payer:\n')                # select the payer
			print('1.\tA0000001\n')                     # option 1 A0000001
			print('2.\tA0000002\n')                     # option 2 A0000002
			payerInput = input('Choice: ')              # get user input for payer, store in payerInput
			print('Select the Payee:\n')                # select the payee
			print('1.\tB0000001\n')                     # option 1 B0000001
			print('2.\tB0000002\n')                     # option 2 B0000002
			payeeInput = input('Choice: ')              # get user input for payee, store in payeeInput
			amountInput = input ('Input the amount of payment in decimal:\n')    # get user input for transaction amount
			txAmount = int(amountInput)      # typecast transaction amount 'amountInput', store in txAmount

			if (payerInput == '1'):                         # check if payerInput is 1 						
				payer = 'A0000001'                          # set payer to account A0000001
				unconfirmedBalance = unconfirmedBalanceA1   # set unconfirmed balance to unconfirmed balance of A0000001
			elif (payerInput == '2'):                       # check if payerInput is 2
				payer = 'A0000002'                          # set payer to account A0000002
				unconfirmedBalance = unconfirmedBalanceA2   # set unconfirmed balance to unonfirmed balance of A0000002
			if (payeeInput == '1'):                         # check if payeeInput is 1
				payee = 'B0000001'                          # set payee to account B0000001
			elif (payeeInput == '2'):                       # check if payeeInput is 2
				payee = 'B0000002'                          # set payee to account B0000002

			if (txAmount + txFee > unconfirmedBalance):       # check if txAmount + txFee > unconfirmedBalance
				print("ERROR: Cannot process transaction. Insufficent funds.\n")     # print error message
			elif (txAmount + txFee <= unconfirmedBalance):        # check if txAmount + txFee <= unconfirmedBalance
				print('Tx: ' + payer + ' pays ' + payee + ' the amount of ' + str(txAmount) + ' BC.\n')
				tx = (payer + payee + hex(txAmount))            # create a transaction and store in tx
				unconfirmedBalance -= (txAmount + txFee)        # update unconfirmedBalance after transaction 
				with open('unconfirmed_T.txt', 'a') as fileUnconfirmedTx:
					fileUnconfirmedTx.write(str(tx) + '\n')         # write tx to unconfirmed_T.txt
				fileUnconfirmedTx.close()
				message = str.encode(str(tx), 'utf-8')          # encode tx and store in message
				clientSocketA.send(message)                     # send message to server
				if (payerInput == '1'):
					unconfirmedBalanceA1 = unconfirmedBalance
				if (payerInput == '2'):
					unconfirmedBalanceA2 = unconfirmedBalance


				# update balance.txt with new unconfirmed balance

		elif (option == '2'):
			print('Option 2 has been selected.\n')
			print('The current balance for each account:\n')
			BalA1 = ('A0000001:'+hex(unconfirmedBalanceA1)+':'+hex(confirmedBalanceA1))
			print(BalA1)
			BalA2 = ('A0000002:'+hex(unconfirmedBalanceA2)+':'+hex(confirmedBalanceA2))
			print(BalA2)
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

	# fileUnconfirmedTx.close()
	fileBalance.close()
	clientSocketA.close()
# end of main()

main()      # call main() driver function




