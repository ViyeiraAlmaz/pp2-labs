#ex 1

def my_generator(n):
    i = 1
    while i <= n:
        yield i**2
        
        i += 1

n = int(input())

for i in my_generator(n):
    print(i)
    
#ex 2

def my_generator(n):
    i = 0
    while i <= n:
        yield i
        i += 2

n = int(input())

for i in my_generator(n):
    print(i)
        
#ex 3
def my_generator(n):
    i = 0
    while i < n:
        if i % 3 == 0 or i % 4 == 0:
            yield i
        i += 1
        
n = int(input())

for i in my_generator(n):
    print(i)
    
    
#ex 4
def squares(a, b):
    while a <= b:
        yield a**2
        a += 1
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)
    
#ex 5

def my_generator(n):
    while n > 0:
        yield n
        n -= 1
n = int(input())
for i in my_generator(n):
    print(i)
