#EX 1
import math
deg = int(input())

rad = int(deg * math.pi)/180
res = rad.around(6)
print(res)

# EX 2
h = int(input())
first_value = int(input())
second_value = int(input())

A = ((first_value + second_value) * h / 2)

print(A)

# EX 3
import math

def area(n, l):
    apothem = l / (2 * math.tan(math.pi / n))
    A = n * apothem * l / 2
    return A


n = int(input())
l = int(input())

result = int(area(n, l))

print(result)


# EX 4

l = int(input())
h = int(input())

def area_of_parallelogram(l, h):
    res = l * h
    return res

area = float(area_of_parallelogram(l, h))
print(area)

