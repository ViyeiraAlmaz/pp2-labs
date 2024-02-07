#1 ex
class Stringj:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())
JJ = Stringj()
JJ.getString()
JJ.printString()
#2 ex
class Shape:
    def init(self):
        pass
    def area(self):
        print("area of the shape:", 0)
class Square(Shape):
    def init(self, length):
        super().init()
        self.length = length
    def area(self):
        print("area of the square:", self.length ** 2)
shape = Shape()
shape.area()
square = Square(int(input()))
square.area() 

#3 ex

class Shape:
    def init(self):
        pass
    def area(self):
        print("Area of the shape:", 0)
class Rectangle(Shape):
    def init(self, length, width):
        super().init()
        self.length = length
        self.width = width
    
    def area(self):
        print("area of the rectangle:", self.length * self.width)
length=float(input())
width=float(input())
rectangle = Rectangle(length, width)
rectangle.area()

#4 ex

import math
class Point:
    def init(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
x1=int(input())
y1=int(input())
point1=Point(x1,y1)
x2=int(input())
y2=int(input())
point2 = Point(x2,y2)
point1.show()
point2.show()
distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)
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
