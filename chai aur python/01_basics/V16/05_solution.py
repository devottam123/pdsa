# Default Parameter Value
# Write a function that greets a user. If no name is provided, it should greet witha default name.
 
def greet(name = "User"):
    return "Hello, "+name+"!"

# person=input()
# print(greet(person))

print(greet("chai"))
print(greet())