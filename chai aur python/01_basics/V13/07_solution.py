order_size = input()
extra_shot = int(input())

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)