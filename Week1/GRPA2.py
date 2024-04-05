def prime(n):
    if (n==1):
        return False
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    return flag

def Goldbach(n):
    l=[]
    m=[]
    for i in range(1,n+1):
        if prime(i):
            l.append(i)
    for i in range(len(l)):
        for j in range(i,len(l)):
            if (l[i]+l[j]==n):
                m.append((l[i],l[j]))
    return m

        
n=int(input())
print(Goldbach(n))
