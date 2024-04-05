# My Solution:
# freq={}
# str=input()
# l=str.split(',')

# for x in l:
#     if x in freq:
#         freq[x]=freq[x]+1
#     else:
#         freq[x]=1

# print(freq)

# Solution:
freq = dict()
L = input().split(',')

for word in L:
    freq[word] = 0

for word in L:
    freq[word] = freq[word] + 1

print(freq)