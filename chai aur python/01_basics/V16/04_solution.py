#Function returning Multiple values.
# Create a function that returns both the area and circumference of a circle given its radius.
import math
def area_and_circum(radius):
    area=math.pi*radius**2
    circum=2*math.pi*radius
    return area, circum

r=int(input())
(area, circumference)=(area_and_circum(r))

print("Area:", round(area,2))
print("Circumference:", round(circumference,2))
