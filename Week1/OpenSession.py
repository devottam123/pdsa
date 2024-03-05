# Week 1 Open Session
class student:
    count=0
    def __init__(self, n, a, c):
        self.name=n
        self.age=a
        self.city=c
        student.count+=1
    def about(self):
        print(self.name)
        print(self.age)
        print(self.city)

s1 = student("Atul", 32, "Delhi")
s2 = student("Amit", 30, "Chennai")

# print(s1)
# print(s1.name)
# print(s2.name)

# print(s1.about())
# print(s2.about())

# print(student.count)
# count is class variable where as name,age and city are object variables.

s1.count+=1 #this again creates a new object
print(s1.count)
print(s2.count)
print(student.count)