# Linear search
def linear_search(L,k):
    for x in L:
        if x==k:
            return True
    return False
# Time Complexity of Linear Search = O(n)

# Binary Search only applies to a Sorted List.
def bSearch(L,k):
    if (L==[]):
        return False
    
    mid=len(L)//2

    if(L[mid]==k):
        return True
    if(L[mid]>k):
        return bSearch(L[:mid],k)
    else:
        return bSearch(L[mid+1:],k)
    
L=[1,2,3,4,5,6,7]
k=1
print(linear_search(L,k))
print(bSearch(L,k))

# Time Complexity of Binary Search = O(log(n))
