#Strings
print("Hello")
print('Hello')

#Assign string to var
x = "hello"
print(x)

#Multiline strings
a = """lorem30vrsvr rvervevrevev
vrevrev
ververververv
vreverv"""
print(a)

#Strings are Arrays
a = "Hello World"
print(a[1])

#Looping through a String
for x in "BOMBACLADDD":
    print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print('free' in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
#Check if NOT
txt =  "The best things in life are free!"
print("expensive" not in txt)

txt =  "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present. ")
    



#Slicing
b = "Hello World"
print(b[2:5])

#slice from the start 
b = 'Hello World'
print(b[:5])

#slice to the end
b = 'Hello World'
print(b[2:])

#negative indexing
b = 'Hello World'
print(b[-5 : -2])



# Upper Case
a = 'Hello World'
print(a.upper())

# Lower Case
a = 'Hello World'
print(a.lower())

# Remove Whitespace
a = ' Hello World '
print(a.strip()) # returns "Hello World"

# Replace String
a = 'Hello World'
print(a.replace("H" , "J"))

# Split String
a = "Hello World"
print(a.split(",")) # returns ['Hello', 'World']


# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
age = 18
txt = "My name is Arsen, and i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))


# Escape Character
txt = "We are the so-called \"Vikings\" from the north."

""" 
\' - single quote
\\ - Backslash
\n - New Line
\r - Carriage Return
\t - Tab
\b - Backspace
\f - Form Feed
\ooo - Octal Value
\xhh - Hex Value
"""



# String Methods
"""
capitalize() - Converts the first character to upper case

casefold() - Converts string into lower case

center() - Returns a centered string

count() - Returns the nuber of times a specified value occurs in a string

encode() - Returns an encoded version of the string

endswith() - Returns true if the string ends with specified value

expandtabs() - Sets the tab size of the string

find() - Searches the string for a specified value and returns the position of where it was found

format() - Formats a specified values in a string

index() - Searches the string for a specified value and returns th eposition where it was found

isalnum() - Returns True if all characters in a string are alphanumeric

isalpha() - Returns True if all characters in a string are in the alphabet

isascii() - Returns True if all characters in a string are in the ascii characters

isdecimal() - Returns True if all characters in a string are in the decimals

isdigit() - Returns True if all characters in a string are in digits

isidentifier() - Returns True if the string is an identifier

islower() - Returns True if all characters in the string are lower case

isnumeric()	- Returns True if all characters in the string are numeric   
    
isprintible() - Returns True if all characters in the string are printable

isspace() - Returns True if all characters in the string are whitespaces

istitle() - Returns True if the string follows the rules of a title

isupper() - Returns True if all characters in the string are upper case
    
join() - Joins the elements of an iterable to the end of the string

ljust() - Returns a left justified version of the string

lower() - Converts a string into lower case

lstrip() - Returns a left trim version of the string

maketrans() - Returns a translation table to be used in translations

partition() - Returns a tuple where the string is parted into three parts

replace() - Returns a string where a specified value is replaced with a specified value

rfind() - Searches the string for a specified value and returns the last position of where it was found

rindex() - Searches the string for a specified value and returns the last position of where it was found

rjust() - Returns a right justified version of the string

rpartition() - Returns a tuple where the string is parted into three parts

rsplit() - Splits the string at the specified separator, and returns a list

rstrip() - Returns a right trim version of the string

split() - Splits the string at the specified separator, and returns a list

splitline() - Splits the string at line breaks and returns a list

startswith() - Returns true if the string starts with the specified value

strip() - Returns a trimmed version of the string

swapcase() - Swaps cases, lower case becomes upper case and vice versa

title() - Converts the first character of each word to upper case

translate() - Returns a translated string

upper() - Converts a string into upper case

zfill() - Fills the string with a specified number of 0 values at the beginning

"""

# PYTHON Strings Exercises
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5] 

txt = " Hello World"
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = 'Hello World'
txt = txt.replace("H", "J")

age = 25
txt = "My name is John Snow, and i am {}"
print(txt.format(age))
