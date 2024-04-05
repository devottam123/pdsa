def binary_search(L, k):
    start = 0
    end = len(L)-1
    mid = (start+end)//2

    if (L==[]):
        return False
    
    if (L[mid]==k):
        return True
    
    if(L[mid]>k):
        return binary_search(L[:mid], k)
    else:
        return binary_search(L[mid+1:], k)
    
print(binary_search([12,34,43,86,99], 12))
    