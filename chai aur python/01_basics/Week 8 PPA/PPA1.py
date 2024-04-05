def traingular(n):
    if(n==1):
        return 1
    return n + traingular(n-1)

n=int(input())
print(traingular(n))