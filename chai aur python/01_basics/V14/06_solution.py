n=int(input())
fact=1
# for i in range(1,n+1):
#     fact=fact*i

# while(n>=1):
while(n>0):
    fact=fact*n
    n-=1

print(fact)