def SelectionSort(L):
    n=len(L)
    if n<1:
        return L
    for i in range(n):
        mpos=i
        for j in range(i+1, n):
            if L[j]<L[mpos]:
                mpos=j
        
        (L[i], L[mpos])=(L[mpos],L[i])
    
    return L

print(SelectionSort([121,32,5,1,66,3,99,32,43]))

# Time Complexity of Selection Sort=O(n^2)
# (In Every Case)

#Best Case Time Complexity = O(n^2)
#Average Case Time Complexity = O(n^2)
#Worst Case Time Complexity = O(n^2)
# Stable = No
# Sort in Place = Yes
