def count(L, word):
    if (len(L)==0):
        return 0
    
    if word==L[0]:
        return 1+count(L[1:], word)
    else:
        return count(L[1:], word)

print(count(['good', 'string', 'good', 'again', 'good'] ,"good"))

print(count(['abc', 'def', 'abcde', 'abc', 'def', 'abc', 'def', 'ghi', 'abc'], "abc"))

print(count(['a', 'an', 'the', 'a', 'an', 'the', 'a', 'an', 'the', 'the', 'an', 'the'], "then"))