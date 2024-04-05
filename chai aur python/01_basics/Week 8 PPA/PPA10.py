def bsearch(L, k):
    if(L==[]):
        return False
    
    mid=len(L)//2

    if(L[mid] == k):
        return True

    if(L[mid]>k):
        return bsearch(L[:mid], k)
    else:
        return bsearch(L[mid+1:], k)
    
print(bsearch([1, 2, 3, 4], 2))
print(bsearch([10, 20, 30, 40, 50], 15))