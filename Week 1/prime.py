def prime(n):
    if(n==1):
        return False
    
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    
    return flag

n=int(input())
print(prime(n))