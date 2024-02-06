# Arithmetic Operators
x = 10
y = 5
print("Arithmetic Operators:")
print("Addition:", x + y)        # Addition
print("Subtraction:", x - y)     # Subtraction
print("Multiplication:", x * y)  # Multiplication
print("Division:", x / y)        # Division
print("Floor Division:", x // y) # Floor Division
print("Exponentiation:", x ** y) # Exponentiation
print("Modulus:", x % y)         # Modulus

# Comparison Operators
print("\nComparison Operators:")
print("Equal to:", x == y)       # Equal to
print("Not Equal to:", x != y)   # Not Equal to
print("Greater than:", x > y)    # Greater than
print("Less than:", x < y)       # Less than
print("Greater than or equal to:", x >= y)  # Greater than or equal to
print("Less than or equal to:", x <= y)     # Less than or equal to

# Logical Operators
a = True
b = False
print("\nLogical Operators:")
print("AND:", a and b)   # AND
print("OR:", a or b)     # OR
print("NOT:", not a)     # NOT

# Assignment Operators
print("\nAssignment Operators:")
x += 1   # Equivalent to x = x + 1
print("Add and Assign:", x)
x -= 1   # Equivalent to x = x - 1
print("Subtract and Assign:", x)
x *= 2   # Equivalent to x = x * 2
print("Multiply and Assign:", x)
x /= 2   # Equivalent to x = x / 2
print("Divide and Assign:", x)

# Membership Operators
list_example = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("In:", 2 in list_example)    # In
print("Not in:", 6 not in list_example)  # Not in

# Identity Operators
x = 10
y = 10
z = [1, 2, 3]
w = [1, 2, 3]
print("\nIdentity Operators:")
print("Is:", x is y)     # Is
print("Is Not:", z is not w)   # Is Not

# Bitwise Operators
p = 10
q = 4
print("\nBitwise Operators:")
print("Bitwise AND:", p & q)     # Bitwise AND
print("Bitwise OR:", p | q)      # Bitwise OR
print("Bitwise XOR:", p ^ q)     # Bitwise XOR
print("Bitwise NOT:", ~p)        # Bitwise NOT
print("Bitwise Left Shift:", p << 2)   # Bitwise Left Shift
print("Bitwise Right Shift:", p >> 2)  # Bitwise Right Shift
