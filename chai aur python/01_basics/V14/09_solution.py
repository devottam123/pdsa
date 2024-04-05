# My solution
# items=["apple", "banana", "orange", "apple", "mango"]

# for i in range(len(items)):
#     for j in range(i+1,len(items)):
#         if items[i]==items[j]:
#             print("Duplicate items found!")
#             break

# Sir's Solution

items=["apple", "banana", "orange", "apple", "mango"]

unique_item=set()

for item in items:
    if item in unique_item:
        print("Duplicate item:", item)
        break
    unique_item.add(item)


