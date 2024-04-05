str =input()
d={}
for x in str:
    if x not in d:
        d[x]=1
    else:
        d[x]=d[x]+1

l=[]
for x in d:
    if d[x]==1:
        l.append(x)

print(l[0])