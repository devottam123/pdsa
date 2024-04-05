def mutiply(a,b):
    if b==1:
        return a
    return a+mutiply(a, b-1)

print(mutiply(5,4))