# def histogram(l):
#     count=0
#     s=set(l)
#     m=[]
#     for x in s:
#         count=0
#         for y in l:
#             if x==y:
#                 count=count+1
#         m.append((x,count))
    
#     return m
        
# L=eval(input())
# print(histogram(L))

l=[(7, 2), (11, 2), (12, 2), (13, 2), (14, 1)]
l.sort(key=l[0][0])
print(l)