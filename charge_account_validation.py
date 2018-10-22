def main():
    # create an empty list
    charge_account = []
    accountfile = open('charge_account.txt', 'r')

    # create a variable to control the loop
    again = 'y'

    # Add some numbers to the list
    while again == 'y':
        # Get account number from the user
        account_number = int(input('Enter charge account number:'))

        # append the account number to the list
        charge_account.append(account_number)

        # Add another number?
        print('Don you ant to add another number?')
        again = input('y = yes, anything else = no:')
        print()
        # Display the numbers that were entered.
        print('Here are the list of charge account numbers you entered')

        for account_number in charge_account:
            print(account_number)
    # Get a charge account number to search for
    search = input('Enter a charge account number to search for:')
    if search not in charge_account:
        print(search, 'Is Invalid')
    else:
        print(search, 'Is valid')

    accountfile.close()


main()

