# My solution
# year = int(input())

# if (year % 400 == 0):
#     print("Leap Year")
# else:
#     if(year % 4==0 and year%4!=100):
#         print("Leap Year")
#     else:
#         print("Not a leap year.")

# Sir's Solution
year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year.")


