# Classes and Objects
# class Point:
#     def __init__(self,a=0,b=0):
#         self.x=a
#         self.y=b
    
#     def translate(self, deltax, deltay):
#         self.x+=deltax
#         self.y+=deltay

#     def odistance(self):
#         import math
#         d = math.sqrt(self.x*self.x + self.y*self.y)
#         return d

#     def __str__(self):
#         return('('+str(self.x)+','+str(self.y)+')')
    
#     def __add__(self,p):
#         return (Point(self.x+p.x,
#                       self.y+p.y))

# p=Point(3,4)
# q=Point(7,10)

# print(p)
# print(p.odistance())
# print(q.odistance())

# print(p+q)

# import math
# class Point:
#     def __init__(self, a=0, b=0):
#         self.r = math.sqrt(a*a + b*b)
#         if a==0:
#             self.theta = math.pi/2
#         else:
#             self.theta = math.atan(b/a)

#     def odistance(self):
#         return (self.r)
    
#     def translate(self,deltax,delaty):
#         x=self.r*math.cos(self.theta)
#         y=self.r*math.sin(self.theta)

#         x+=deltax
#         y+=delaty

#         self.r=math.sqrt(x*x+y*y)
#         if x==0:
#             self.theta=math.pi/2
#         else:
#             self.theta=math.atan(y/x)

# p=Point(3,4)
# q=Point(7,10)

# print(p)
# print(p.odistance())
# print(q.odistance())
# print(p.r)
# print(p.theta)


