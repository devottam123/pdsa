# # Checking Primality

# def factors(n):
#     fl=[]    #factors list
#     for i in range(1, n+1):
#         if (n%i)==0:
#             fl.append(i)
#     return fl

# def prime(n):
#     return (factors(n) == [1,n])
    
# # print(prime(5))

# # Counting primes
# def primesupto(m):
#     pl=[]       #prime list
#     for i in range(1, m+1):
#         if prime(i):
#             pl.append(i)
#     return pl

# # print(primesupto(50))

# def firstprimes(m):
#     (count, i, pl) = (0,1,[])
#     while(count<m):
#         if prime(i):
#             (count, pl) = (count+1, pl + [i])
#         i=i+1
#     return(pl)

# print(firstprimes(25))

# def prime(n):
#     result = True
#     for i in range(2,n):
#         if (n%i)==0:
#             result=False
#             break       #Abort loop
#     return result

# print(prime(20))

# def prime(n):
#     (result, i) = (True, 2)
#     while(result and i<n):
#         if (n%i) == 0:
#             result = False
#         i=i+1
#     return result

# print(prime(5))

import math
def prime(n):
    (result, i) = (True, 2)
    while(result and i<math.sqrt(n)):
        if (n%i) == 0:
            result = False
        i=i+1
    return result

# print(prime(80))

# If the difference between the two prime numbers is 2, then they are known as Twin Primes.
# They are of the form 2^k-1 and 2^k+1.

# Finding numbers of differences in primes upto n
# Key: Difference Value
# Value: No. of differences of that value.
def primediffs(n):
    lastprime=2
    pd={}   #Dictionary for prime differences
    for i in range(3, n+1):
        if prime(i):
            d=i-lastprime
            lastprime=i
            if d in pd.keys():
                pd[d]=pd[d]+1
            else:
                pd[d]=1
    return pd

print(primediffs(10))
