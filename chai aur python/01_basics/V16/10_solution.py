# Recursive Function
# Create a recursive function to calculate the factorial of a fucntion.

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(6))