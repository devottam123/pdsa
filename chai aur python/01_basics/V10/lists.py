# tea_varieties = ["Black", "Green", "Oolong", "White"]
# print(tea_varieties)

# print(tea_varieties[0])
# print(tea_varieties[1])
# print(tea_varieties[-1])
# print(tea_varieties[1:3])
# print(tea_varieties[:2])
# print(tea_varieties[2:])
# print(tea_varieties[3])
# tea_varieties[3] = "Herbal"
# print(tea_varieties)
# tea_varieties[1:2] = "Lemon" #don't change variables like this in lists in python
# "Lemon" is treated like an array and given to tea_variables[1:2], that's why answer is coming ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'White']
# print(tea_varieties)
# tea_varieties[1:2] = ["Lemon"]
# print(tea_varieties)
# print(tea_varieties[1:3])
# tea_varieties[1:3] = ["green", "masala"]
# print(tea_varieties)

# print(tea_varieties[1:1])
# tea_varieties[1:1] = ["test", "test"]
# print(tea_varieties)

# print(tea_varieties[1:2])
# print(tea_varieties[1:3])
# tea_varieties[1:3] = [] #inserting nothing or delete operation through slicing
# print(tea_varieties)

# for tea in tea_varieties:
#     print(tea)

# for tea in tea_varieties:
#     print(tea, end="-")

# if "Oonlong" in tea_varieties:
#     print("I have Oolong Tea.")

# tea_varieties.append("Oolong")
# if "Oolong" in tea_varieties:
#     print("I have Oolong Tea.")

# print(tea_varieties)
# tea_varieties.pop()
# print(tea_varieties)

# tea_varieties.remove("green")
# print(tea_varieties)

# tea_varieties.insert(1, "green")
# print(tea_varieties)

# tea_varieties_copy = tea_varieties
# tea_varieties[1]="oolong"
# print(tea_varieties)
# print(tea_varieties_copy)

# tea_varieties_copy1 = tea_varieties.copy()
# print(tea_varieties_copy1)
# tea_varieties_copy1.append("lemon")
# print(tea_varieties_copy1)
# print(tea_varieties_copy)
# print(tea_varieties)

# print(range(10))
# y = range(10)
# print(y)
# squared_nums = [x**2 for x in range(10)]
# print(squared_nums)
# cube_num = [y**3 for y in range(5)]
# print(cube_num)

# l=[1,2,4,6,45,454,5]
# l.pop()
# print(l)
# l.pop(3)
# print(l)

l=[1,2,4,6,45,454,5]
l.insert(2,99)
print(l)

l.reverse()
print(l)

l.sort()
print(l)


l.sort(reverse=True)
print(l)
