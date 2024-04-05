# tea_types = ()
# print(tea_types)
# print(type(tea_types))

tea_types = ("Black", "Green", "Oolong")
# print(tea_types)
# print(tea_types[0])
# print(tea_types[-1])
# print(tea_types[1:])

# tea_types[0]= "Lemon" 
#This will give error as Tuples are immutable

# print(len(tea_types))

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
# print(all_tea)

# if "Green" in all_tea:
#     print("I have Green Tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")
# more_tea = ["Herbal", "Earl Grey", "Herbal"]
# print(more_tea)
# print(more_tea.count("Herbal"))
# print(more_tea.count("Herb"))

(black, green, oolong) = tea_types
# print(black)
# print(green)
# print(oolong)
# print(type(tea_types))

x= ("hi", (1,2,3), "Hemllo")
print(x[0])
print(x[1])
print(x[2])