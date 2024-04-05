def value_to_keys(D, value):
    l=[]
    for key in D:
        if value==D[key]:
            l.append(key)
    return l      

print(value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10))
print(value_to_keys({'good': 'boy', 'great': 'expectations'}, 'great'))
print(value_to_keys({1: 10, 2: 10, 3: 10, 4: 10, 5: 10}, 10))
print(value_to_keys({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 1, 'g': 1}, 1))
print(value_to_keys({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 1, 'g': 1}, 10))
print(value_to_keys({1: 'a', 2: 'b', 3: 'a', 4: 'a', 5: 'f', 6: 'f', 7: 'b'}, 'a'))
print(value_to_keys({1: 'a', 2: 'b', 3: 'a', 4: 'a', 5: 'f', 6: 'f', 7: 'b'}, 'b'))


