# def gcd(m,n):
#     (a,b)=(max(m,n), min(m,n))
#     if a%b==0:
#         return b
#     else:
#         return(gcd(b,a-b))

# print(gcd(4,12))
# Unfortunately, this takes time proportional to max(m,n)

# Euclid's Algorithm

def gcd(m,n):
    (a,b)=(max(m,n), min(m,n))
    if a%b==0:
        return b
    else:
        return(gcd(b,a%b))

print(gcd(3,10))

# This takes time proportional to number of digits in max(m,n)
