a=int(input())
b=int(input())
try:
    f=open('abc.txt', 'r')
    c=a/b
    print(c)
    # print(d)
    # f.close()
except ZeroDivisionError:
    # pass
    print("Invalid input, divisor cannot be zero!")
# except NameError:
#     print("Variable not defined!")
# except FileNotFoundError:
#     print("Invalid file name. Please check again!")
except:
    print("Something went wrong!")
finally:
    f.close()
    print("File closed!")

