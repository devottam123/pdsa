# My Solution:
def non_decreasing(L):
    if (len(L)==2):
        if (L[-1]>=L[-2]):
            return True
        else:
            return False

    if (L[-1]>=L[-2]):
        return non_decreasing(L[:-1])
    else:
        return False
    
print(non_decreasing([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10]))

# Solution:
def non_decreasing(L):
    if len(L) <= 1:
        return True
    if L[-2] > L[-1]:
        return False
    return non_decreasing(L[:-1])