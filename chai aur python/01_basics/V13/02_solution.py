# My Solution:
# age = int(input())
# day = input()

# if (day=="Wednesday"):
#     if(age<18):
#         print("Price for your ticket is: $6")
#     else:
#         print("Price for your ticket is: $10")
# else:
#     if(age<18):
#         print("Price for your ticket is: $8")
#     else:
#         print("Price for your ticket is: $12")

# Sir's Solution:
age = int(input())
day = input()

price = 12 if age >=18 else 8

if day == "Wednesday":
    # price = price -2
    price -= 2

print("TIcket price for you is: $", price)




