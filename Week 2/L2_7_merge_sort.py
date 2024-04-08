def merge(A,B):
    (m,n)=(len(A), len(B))
    (C,i,j,k)=([],0,0,0)

    while(k<m+n):
        if i==m:
            C.extend(B[j:])
            k=k+(n-j)

        elif j==n:
            C.extend(A[i:])
            k=k+(n-i)

        elif(A[i]<B[j]):
            C.append(A[i])
            (i,k)=(i+1, k+1)
        else:
            C.append(B[j])
            (j,k)=(j+1, k+1)
    
    return C

def merge_sort(A):
    n=len(A)

    if n<=1:
        return A

    L=merge_sort(A[:n//2])
    R=merge_sort(A[n//2:])

    B=merge(L,R)

    return B

print(merge_sort([121,32,5,1,66,3,99,32,43]))
    
# Time Comlexity of Merge Sort = O(nlog(n))
# (In every Case)

#Best Case Time Complexity = O(nlog(n)) 
#Average Case Time Complexity = O(nlog(n))
#Worst Case Time Complexity = O(nlog(n))
