def isort(L):

    min=L[0]
    for x in L:
        if x<min:
            min=x
    L.remove(min)
    return [min]+L    

print(isort([1, 5, 4, 3, 2]))