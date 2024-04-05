species = input()
age = int(input())

if species.lower() == "dog":
    if age<2:
        print("Puppy Food")
    else:
        print("Senior Dog Food")
elif(species.lower() =="cat"):
    if age<=5:
        print("Baby Cat Food")
    else:
        print("Senior Cat Food")