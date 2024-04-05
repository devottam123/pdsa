def factors(m):
    l=[]
    for i in range(1,m+1):
        if m%i==0:
            l.append(i)
    return l
    
n=int(input())
print(factors(n))