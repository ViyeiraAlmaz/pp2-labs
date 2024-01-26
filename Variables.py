x = 5 
y = "John"
print(x)
print(y)

x = 4            # x is of type int
x = "Sally"      # x is of tupe str
print (x)

x = str(3)  #x will be "3"
y = int(3)  #y will be 3
z = float(3) # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

# Many values to multiple variables
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "orange"
print(x)
print(y)
print(z)

# Unpack a collection 
fruits = ["apple", "banana", "watermelon"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "python is awesome"
print(x)

x = "python"
y = "is"
z = "awesome"
print(x, y, z)

x = "python "
y = 'is '
z = 'awesome'
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x + y) #error

x = 5
y = "John"
print(x, y)

#var
x = 'awesome'
def myfunc():
    print("Puthon is " + x)
    
myfunc()

#inside var
x = 'awesome'
def myfunc():
    x = 'bombacladd'
    print("Puthon is " + x)
    
myfunc()
print("Puthon is " + x)

#global var
def myfunc():
    global x
    x = "bombalcadd"
    
myfunc()

print("Python is " + x)

#exercise
carname = "Mersedes-Benz"

x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "orange" , "banana" , "watermelon"

x = y = z = "banana"

def myfunc():
    global x
    x = "bombacladd"

