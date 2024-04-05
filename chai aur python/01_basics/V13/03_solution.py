# My Solution
# score = int(input("Enter your Score: "))

# if(score > 89 and score<=100):
#     print("A")
# elif(score>79):
#     print("B")
# elif(score>69):
#     print("C")
# elif(score>59):
#     print("D")
# else:
#     print("F")

# Sir's Solution
score = int(input())

if score >= 101:
    print("Please verify your grade again.")
    exit()

if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else:
    grade = "F"

print("Grade:",grade)

