#ex1
import math, time
def llist(list1):
    return math.prod(list1)
print(llist([1,2,3,4,5]))
print()

#ex2
def strins(strs):
    upperc=sum(1 for ch in strs if ch.isupper())
    lowerc=sum(1 for ch in strs if ch.islower())
    return upperc,lowerc
strs="This is NOT AvAible"
upperc,lowerc=strins(strs)
print("This is UPPERCASES:>",upperc)
print("This is lowercases:>",lowerc)
print()

#ex3
def stringgs(strs):
    return "True" if strs==strs[::-1] else "False"
print(stringgs("abba"))
print(stringgs("abbd"))
print()

#ex4
def root_after_ms(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)
num = 25100
ms = 2123
print(f"Square root of {num} after {ms} miliseconds is {root_after_ms(num, ms)}")
print()

#ex5
def thisistuple(tupl):
    x=all(tupl)
    return x
print(thisistuple((1,2,3,4)))
print(thisistuple((False,True)))
print(thisistuple(("thisisstring",1234)))
