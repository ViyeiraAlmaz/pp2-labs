#1 ex
class Stringj:
    def __init__(s):
        s.input_string = ""

    def getString(s):
        s.input_string = input()

    def printString(s):
        print(s.input_string.upper())
JJ = Stringj()
JJ.getString()
JJ.printString()
#6 ex
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input().split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
#5 ex
class Account:
    def __init__(s, owner, balance=0):
        s.owner = owner
        s.balance = balance

    def deposit(s, amount):
        s.balance += amount
        print(f"Deposit of ${amount} accepted. New balance: ${s.balance}")

    def withdraw(s, amount):
        if amount <= self.balance:
            s.balance -= amount
            print(f"Withdrawal of ${amount} accepted. New balance: ${s.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

owner_name = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account = Account(owner_name, initial_balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        deposit_amount = float(input("Enter the deposit amount: "))
        account.deposit(deposit_amount)
    elif choice == '2':
        withdraw_amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(withdraw_amount)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


#6 ex
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input().split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
