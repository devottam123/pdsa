n=int(input())
scores_dataset=[]
for i in range(n):
    D={}
    D["Name"]=input()
    D["City"]=input()
    D["SeqNo"]=int(input())
    D["Mathematics"]=int(input())
    D["Physics"]=int(input())
    D["Chemistry"]=int(input())
    scores_dataset.append(D)

print(scores_dataset)





