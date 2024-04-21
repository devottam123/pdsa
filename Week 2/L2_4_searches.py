# Linear search
def linear_search(L,k):
    for x in L:
        if x==k:
            return True
    return False
# Time Complexity of Linear Search = O(n)

# Binary Search only applies to a Sorted List.
# def bSearch(L,k):
#     if (L==[]):
#         return False
    
#     mid=len(L)//2

#     if(L[mid]==k):
#         return True
#     if(L[mid]>k):
#         return bSearch(L[:mid],k)
#     else:
#         return bSearch(L[mid+1:],k)
    
# L=[1,2,3,4,5,6,7]
# k=1
# print(linear_search(L,k))
# print(bSearch(L,k))

# Time Complexity of Binary Search = O(log(n))
# The above method is not so efficient because Due to slicing, this implimentation takes O(n) time more.
# So, total time complexity becomes = O(log(n) +n) = O(n)


# So, it's correct implemetation:
# Iterartive Implementation
def binarysearch(L, v):
    low = 0
    high = len(L) - 1
    while (low <= high):
        mid = (low + high) // 2
        if L[mid] < v:
            low = mid - 1
        elif L[mid]>v:
            high=mid - 1
        else:
            return mid
    return False

# L=[1,2,3,4,5,6,7]
# k=1
# print(binarysearch(L,k))            
            
# Recursive Implementation
def bSearch(L,v,low,high):
    if high - low < 0:
        return False
    
    mid=(high + low) // 2

    if v == L[mid]:
        return mid
    if v < L[mid]:
        return(bSearch(L, v, low, mid-1))
    else:
        return(bSearch(L,v,mid+1,high))
    
L=[1,2,3,4,5,6,7]
k=7
print(bSearch(L,k,0,len(L)-1))    