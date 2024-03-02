#Computing GCD
# def gcd(m,n):
#     cf=[]    #List of common factors
#     for i in range(1, min(m,n)+1):
#         if (m%i)==0 and (n%i)==0:
#             cf.append(i)
#     return cf[-1]

# print(gcd(8,12))

def gcd(m,n):
    for i in range(1, min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            mrcf=i
    return mrcf

print(gcd(8,12))

# Both the functions have equal time complexity.