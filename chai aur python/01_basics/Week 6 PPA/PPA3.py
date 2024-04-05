def is_key(D, key):
    if key in D.keys():
        return True
    return False

def value(D, key):
    if key in D.keys():
        return D[key]
    return None
    
print(is_key({'good': 4, 'day': 3}, 'good'))
print(value({'good': 4, 'day': 3}, 'day'))
print(is_key({1: 2, 3: 4, 5: 6, 7: 8}, 3))
print(is_key({1: 2, 3: 4, 5: 6, 7: 8}, 10))
print(value({1: 2, 3: 4, 5: 6, 7: 8}, 3))
print(value({1: 2, 3: 4, 5: 6, 7: 8}, 100))
print(is_key({'good': 'day', 'how': 'wow', 'some': 'none'}, 3))
print(is_key({'good': 'day', 'how': 'wow', 'some': 'none'}, 'some'))
print(value({'good': 'day', 'how': 'wow', 'some': 'none'}, 'some'))
print(value({'good': 'day', 'how': 'wow', 'some': 'none'}, 'something')	)