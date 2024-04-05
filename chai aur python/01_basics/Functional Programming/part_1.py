# fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

# # for fruit in fruits:
# #     print(fruit)

# basket = iter(fruits)
# print(basket)
# print(basket.__next__())
# print(basket.__next__())
# print(basket.__next__())
# print(basket.__next__())
# print(next(basket))
# print(next(basket))
# print(next(basket))
# print(next(basket))
# print(next(basket))

# yield
def square(limit): #This function is called a Generator
    x = 0
    while x < limit:
        yield x*x
        yield x*x*x
        x += 1

a = square(5)
print(next(a), next(a)) 
print(next(a), next(a)) 
print(next(a), next(a)) 
print(next(a), next(a)) 

