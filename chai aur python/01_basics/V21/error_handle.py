file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

#the above code is same as the code given below. below code automatically closes the file after execution of the code within scope of with open('youtube.txt', 'w') as file
with open('youtube.txt', 'w') as file:
       file.write('chai aur python')