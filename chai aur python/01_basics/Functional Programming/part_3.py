# Lambda Functions

# add = lambda x,y: x+y

# sub = lambda x,y: x-y

# mul = lambda x,y: x*y

# div = lambda x,y: x/y

# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))
# print(div(10,20))
# print(type(mul))

# *************************
# Enumerate Functions & Zip Function
fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

size = [5, 5, 6, 6, 9, 10, 5, 4]

# for fruit in enumerate(fruits):
#     print(fruit)

# print(list(zip(fruits, size)))
# print(dict(zip(fruits, size)))
# print(set(zip(fruits, size)))
# print(tuple(zip(fruits, size)))

# Without using zip function:
# l=[]
# for i in range(len(fruits)):
#     for j in range(len(size)):
#         if i==j:
#             l.append((fruits[i], size[i]))
#             break
# print(l)

# *********************************************
# map function
a=[10, 20, 30, 40, 50, 60]
b=[5, 10, 15, 20, 25, 30]
# c=a-b #this will give an error

def sub(x,y):
    return x-y

def increament(x):
    return x + 1

# c = map(sub, a, b)
# c= map(increament, a)
# print(list(c))   

# *************************************
# map and filter function
import math

a=[25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    if n>=0:
        return n
    
c=map(square_root, filter(is_positive, a))

print(list(c))






