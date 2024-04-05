# a = 100
# b = 20
# # if a<b:
# #     small=a
# # else:
# #     small=b

# small = a if a<b else b

# ***********************************
# print(small)

# a=5
# while a>0: print(a); a-=1

# ************************************
# List Comprehension
fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

# newlist=[]
# for fruit in fruits:
#     if 'n' in fruit:
#         newlist.append(fruit.capitalize())

newlist=[fruit.capitalize() for fruit in fruits if 'n' in fruit]

print(newlist)





