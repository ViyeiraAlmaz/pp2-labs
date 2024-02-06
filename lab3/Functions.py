import random
#2nd ex
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit = float(input())
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)

#3rd ex
def find(numheads, numlegs):
    rab = (numlegs - (2 * numheads))/2
    chi = numheads - rab
    return int(rab), int(chi)
    
numheads = 35
numlegs = 94
rabbits, chickens = find(numheads, numlegs)
print("Number of rabbits: ", rabbits)
print("Number of chickens: ", chickens)
#4th ex
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

user_input = input()
numbers = list(map(int, user_input.split()))

prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)
#6th ex
def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence
user_input = input()

reversed_sentence = reverse_sentence(user_input)

print(reversed_sentence)
#7th task
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input()
nums = list(map(int, user_input.split()))

result = has_33(nums)

if result:
    print("True")
else:
    print("False")
#8th ex
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

user_input = input()
nums = list(map(int, user_input.split()))

result = spy_game(nums)

if result:
    print("True")
else:
    print("False")
#9th ex
import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)
radius = float(input())
volume = sphere_volume(radius)
print(volume)
#10th ex
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
user_input = input()
input_list = list(map(int, user_input.split()))
unique_list = unique_elements(input_list)
print(unique_list)
#11 ex
#Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def ispalindrom():
    s=input()
    return s==s[::-1]
print(ispalindrom())

#12 ex
#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram():
    nums=list(map(int,input().split()))
    for i in nums:
        print('*'*i, end=" ")
histogram()
print("\n")

#13 ex
"""Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal
Hello! What is your name? KBTU Well, KBTU, I am thinking of a number between 1 and 20. Take a guess. 12 Your guess is too low. Take a guess. 16 Your guess is too low. Take a guess. 19 Good job, KBTU! You guessed my number in 3 guesses!"""
def whats_the_number():
    name=input()
    print("Hello! What is your name?")
    print(f"{name} Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number=random.randint(1,20)
    number=0
    while True:
        print("Take a guess")
        number+=1
        guess=int(input())
        if guess<secret_number:
            print("Your guess is too low.")
        elif guess>secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, KBTU!, You guessed my number in {number} guesses!")
            break
whats_the_number()
