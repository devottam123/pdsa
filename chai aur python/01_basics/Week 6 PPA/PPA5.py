# My solution:
# def dict_to_list(D):
#     l=[]
#     for key in D:
#         l.append((key, D[key]))
#     return l

# def list_to_dict(L):
#     D={}
#     for x in L:
#         key=x[0]
#         value=x[1]
#         if key not in D:
#             D[key]=value
#     return D

# Solution:
def dict_to_list(D):
    L = [ ]

    for key in D:
        L.append((key, D[key]))

    return L

def list_to_dict(L):
    D = dict()

    for key, value in L:
        D[key] = value

    return D

print(dict_to_list({'abc': 3, 'def': 10}))
print(list_to_dict([('def', 10), ('abc', 3)]))
print(dict_to_list({'1': 'one', '2': 'two', '3': 'three', '4': 'four'}))
print(list_to_dict([('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')]))
print(dict_to_list({1: 2, 3: 4, 5: 6, 7: 8}))
print(list_to_dict([(1, 2), (3, 4), (5, 6), (7, 8)]))
print(dict_to_list({'pot': 'top', 'ate': 'eta', 'lie': 'eil', 'tup': 'put'}))
print(list_to_dict([('ate', 'eta'), ('lie', 'eil'), ('pot', 'top'), ('tup', 'put')]))