# Function with *args
# Write a function that takes variable number of arguements and returns their sum.

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2, 3, 4, 5))
# print(sum_all(1,2, 3, 4, 5, 6, 7, 8))


# def sum_all(*chai):
#     return sum(chai)
# # but we should only write args as it is a good practice.
# print(sum_all(1,2))
# print(sum_all(1,2, 3, 4, 5))
# print(sum_all(1,2, 3, 4, 5, 6, 7, 8))

def sum_all(*args):
    # print(*args)
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2, 3, 4, 5))
# print(sum_all(1,2, 3, 4, 5, 6, 7, 8))