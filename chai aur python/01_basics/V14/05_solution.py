# My solution
# str =input()
# d={}
# for x in str:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1

# l=[]
# for x in d:
#     if d[x]==1:
#         l.append(x)

# print(l[0])

# Sir's Solution
input_str=input()

for char in input_str:
    if input_str.count(char)==1:
        print("Char is:", char)
        break

