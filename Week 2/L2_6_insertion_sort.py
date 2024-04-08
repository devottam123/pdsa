def InsertionSort(L):
    n=len(L)
    if n<1:
        return L
    
    for i in range(n):
        # Assume L[:i] to be a sorted list
        # Move L[i] to correct position in L 
        j=i
        while(j>0 and L[j-1]>L[j]):
            (L[j],L[j-1])=(L[j-1],L[j])
            j=j-1
            #Now L[:i+1] is sorted
    return L

print(InsertionSort([121,32,5,1,66,3,99,32,43]))

# Time Comlexity of Insertion Sort = O(n^2)

#Best Case Time Complexity = O(n) => List already sorted, Inset stops in 1 step
#Average Case Time Complexity = O(n^2)
#Worst Case Time Complexity = O(n^2)

