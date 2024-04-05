L = input().split(',')

real_dict={}

for word in L:
    key = word[0]
    if key not in real_dict:
        real_dict[key]=[]
    real_dict[key].append(word)
    
print(real_dict)
    




