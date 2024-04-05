def odd_one(L):
    for i in range(len(L)):
        if type(L[0])==type(L[1]):
            if type(L[i])!=type(L[0]):
                return type(L[i]).__name__
        else:
            return type(L[0]).__name__    
print(odd_one(eval(input().strip())))


