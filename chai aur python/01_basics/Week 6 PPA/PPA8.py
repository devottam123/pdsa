# s=set()
# s.add(1)
# s.add(2)
# print(s)

def factors(n):
    s=set()
    for i in range(1,n+1):
        if (n%i==0):
            s.add(i)
    return s

def common_factors(a,b):
    A=factors(a)
    B=factors(b)
    return A & B

def factors_upto(n):
    D={}
    for i in range(1,n+1):
        D[i]=factors(i)
    return D

print(factors(10))
print(common_factors(10,5))
print(factors_upto(4))
print(factors(20))
print(common_factors(100,200))
print(factors_upto(10))







