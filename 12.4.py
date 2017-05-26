class Customer:
    """Customer object has attributes that are used as ID, PIN, and
     saving and checking accounts."""
    def __init__(self, ID, PIN):
        self.ID = ID
        self.PIN = PIN
        self.sav_acc = []
        self.che_acc = []
        self.info = {self.ID: {self.PIN: [[self.sav_acc], [self.che_acc]]}}


try:
    with open('atm_info.txt') as f:
        ID, PIN = f.readline().strip().split()
        c = Customer(ID, PIN)
        c.sav_acc = [float(x) for x in f.readline().strip().split()]
        c.che_acc = [float(x) for x in f.readline().strip().split()]
        customers = [c]
except ValueError:
    print("Need to fill in file properly.")


def get_info():
    print("Welcome to PyBank.")
    print()
    user_ID = input("Please enter your user ID: ")
    PIN = input("Please enter your PIN: ")
    print()
    return user_ID, PIN


def print_choices():
    print('To check an account balance, enter "C"')
    print('To make a withdrawal, enter "W"')
    print('To transfer money between accounts, enter "T"')
    print('To exit, enter "X"')
    choice = input('What would you like to do? ').upper()
    print()
    return choice


def check_balance(customer):
    print("For the balance of your savings account, enter 'S'")
    print("For the balance of your checking account, enter 'C'")
    print("For the balance of both, enter 'B'")
    print("To exit this menu, enter 'X'")
    choice = input('What would you like to do? ').upper()
    print()
    if choice == 'S':
        print(f'savings account balance: ${customer.sav_acc[-1]:.2f}\n')
    elif choice == 'C':
        print(f'checking account balance: ${customer.che_acc[-1]:.2f}\n')
    elif choice == 'B':
        print(f'savings account balance:'
              f' ${customer.sav_acc[-1]:.2f}\n'
              f'checking account balance:'
              f' ${customer.che_acc[-1]:.2f}\n')
    elif choice == 'X':
        print("Se ya!")
    else:
        print("Invalid choice!")


def withdrawal(customer):
    print(f'savings account balance: ${customer.sav_acc[-1]:.2f}')
    print(f'checking account balance: ${customer.che_acc[-1]:.2f}')
    print()
    print("To withdraw from your savings account, enter 'S'")
    print("To withdraw from your checking account, enter 'C'")
    print("To exit this menu, enter 'X'")
    choice = input('What would you like to do? ').upper()
    print()
    if choice == 'S':
        account = customer.sav_acc
        word = 'savings'
    elif choice == 'C':
        account = customer.che_acc
        word = 'checking'
    elif choice == 'X':
        print("Se ya!")
    else:
        print("Invalid choice!")
    try:
        if account[-1] > 0:
            amount = float(input("How much would you like to withdraw? "))
            print()
            if amount > account[-1]:
                print(f"You don't have that much money in your {word}.")
                print(f"Withdrawing all from {word} account.")
                print(f"Now dispensing ${account[-1]:.2f}")
                account.append(0)
                print(f'{word} account balance: ${account[-1]:.2f}')
            elif amount < 0:
                print("Can't withdraw negative amounts.\n")
            else:
                print(f"Now dispensing ${amount:.2f}\n")
                new_balance = account[-1] - amount
                account.append(new_balance)
                print(f'{word} account balance: ${account[-1]:.2f}\n')
        else:
            print(f"You can't withdraw from an empty {word} account.")
    except UnboundLocalError:
        pass


def transfer(customer):
    print(f'savings account balance: ${customer.sav_acc[-1]:.2f}')
    print(f'checking account balance: ${customer.che_acc[-1]:.2f}')
    print()
    print("To transfer from your savings account, enter 'S'")
    print("To transfer from your checking account, enter 'C'")
    print("To exit this menu, enter 'X'")
    choice = input('What would you like to do? ').upper()
    print()
    if choice == 'S':
        account = customer.sav_acc
        other = customer.che_acc
        words = ['savings', 'checking']
    elif choice == 'C':
        account = customer.che_acc
        other = customer.sav_acc
        words = ['checking', 'savings']
    elif choice == 'X':
        print("Se ya!")
    else:
        print("Invalid choice!")
    try:
        if account[-1] > 0:
            amount = float(input("How much would you like to transfer? "))
            print()
            if amount > account[-1]:
                print(f"You don't have that much money in your {words[0]}.")
                print(f"Withdrawing all from {words[0]} account.")
                print(f"Now transferring ${account[-1]:.2f}\n")
                new_balance = other[-1] + account[-1]
                other.append(new_balance)
                account.append(0)
                print(f'{words[0]} account balance: ${account[-1]:.2f}')
                print(f'{words[1]} account balance: ${other[-1]:.2f}')
                print()
            elif amount < 0:
                print("Can't transfer negative amounts.\n")
            else:
                print(f"Now transferring ${amount:.2f}\n")
                new_balance = account[-1] - amount
                account.append(new_balance)
                other_new_balance = other[-1] + amount
                other.append(other_new_balance)
                print(f'{words[0]} account balance: ${account[-1]:.2f}')
                print(f'{words[1]} account balance: ${other[-1]:.2f}')
                print()
        else:
            print(f"You can't transfer from an empty {words[0]} account.")
    except UnboundLocalError:
        pass


def main():
    while True:
        user_ID, PIN = get_info()
        for customer in customers:
            if user_ID == customer.ID and PIN == customer.PIN:
                c = customer
        break
    while True:
        choice = print_choices()
        if choice == 'C':
            check_balance(c)
        elif choice == 'W':
            withdrawal(c)
        elif choice == 'T':
            transfer(c)
        elif choice == 'X':
            with open('atm_info.txt', 'w') as f:
                f.write(f"{user_ID} {PIN}\n")
                f.write(' '.join([str(x) for x in c.sav_acc]))
                f.write('\n')
                f.write(' '.join([str(x) for x in c.che_acc]))
                f.write('\n')
            print("Se ya!")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
