distance = int(input())

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommeds you the transport of:", transport)
