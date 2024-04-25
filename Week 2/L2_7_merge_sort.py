# def merge(A,B):
#     (m,n)=(len(A), len(B))
#     (C,i,j,k)=([],0,0,0)

#     while(k<m+n):
#         if i==m:
#             C.extend(B[j:])
#             k=k+(n-j)

#         elif j==n:
#             C.extend(A[i:])
#             k=k+(n-i)

#         elif(A[i]<B[j]):
#             C.append(A[i])
#             (i,k)=(i+1, k+1)
#         else:
#             C.append(B[j])
#             (j,k)=(j+1, k+1)
    
#     return C

# def merge_sort(A):
#     n=len(A)

#     if n<=1:
#         return A

#     L=merge_sort(A[:n//2])
#     R=merge_sort(A[n//2:])

#     B=merge(L,R)

#     return B

# print(merge_sort([121,32,5,1,66,3,99,32,43]))

# Better Implementation:-
def merge(A,B):
    (m,n) = (len(A), len(B))
    (C, i, j) = ([], 0, 0)

    # Case 1 :- When both lists A and B have elements for comparing
    while i<m and j<n:
        if A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        else:
            C.append(B[j])
            j=j+1

    # Case 2 :- If list B is over, shift all elements of A to C
    while i<m:
        C.append(A[i]) 
        i=i+1

    #Case 3 :- If list A is over, shift all elements of B to C  
    while j<n:
        C.append(B[j])
        j=j+1
    
    # Return sorted merged list
    return C


# Recursively divide the problem into sub-problems to sort the input list L    
def mergesort(L):
    n=len(L)

    if n<=1:  # If the list contains only one element or is empty return the list.
        return L

    Left_Half = mergesort(L[:n//2]) # Recursively sort the left half of the list
    Right_Half = mergesort(L[n//2:]) # Recursively sort the right half of the list

    Sorted_Merged_List = merge(Left_Half, Right_Half) # Merge two sorted list Left_Half and Right_Half

    return(Sorted_Merged_List)

print(mergesort([121,32,5,1,66,3,99,32,43]))
   
# Time Comlexity of Merge Sort = O(nlog(n))
# (In every Case)

# Best Case Time Complexity = O(nlog(n)) 
# Average Case Time Complexity = O(nlog(n))
# Worst Case Time Complexity = O(nlog(n))
# Stable = Yes
# Sort in Place = No