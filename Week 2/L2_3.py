# Maximum element in a list
# def maxElement(L):
#     maxval=L[0]
#     for i in range(len(L)):
#         if L[i]>maxval:
#             maxval=L[i]
#     return maxval

# L=eval(input())
# print(maxElement(L))

# finding duplicates
# def noDuplicates(L):
#     for i in range(len(L)):
#         for j in range(i+1, len(L)):
#             if L[i]==L[j]:
#                 return False
#     return True


# print(noDuplicates([1,2,3,6,2,9]))

# Matrix Multiplication

# def matrixMultiplication(A,B):
#     (m,n,p)=(len(A), len(B), len(B[0]))

#     C=[[0 for i in range(p)]
#        for j in range(m)]
    
#     for i in range(m):
#         for j in range(p):
#             for k in range(n):
#                 C[i][j] = C[i][j]+A[i][k]*B[k][j]
    
#     return C

# A=[[1,2,3],[4,5,6]]
# B=[[7,8,9],[10,11,12]]

# print(matrixMultiplication(A,B))


# Number of bites Binary representation of n
def numberOfBites(n):
    
    count=1

    while (n>1):
        count=count+1
        n=n//2

    return count 

print(numberOfBites(5))
