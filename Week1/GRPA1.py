def find_Min_Difference(L,P):
    L=sorted(L)
    head=0
    tail=P-1
    min_diff=L[tail]-L[head]
    while(tail<len(L)):
        if ((L[tail]-L[head])<min_diff):
            min_diff=(L[tail]-L[head])
        tail=tail+1
        head=head+1
    return min_diff


L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))