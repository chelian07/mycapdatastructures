#TASK 1
print('TASK 1')
import math
radius= int(input('Input the radius of the circle :'))  
area = math.pi*radius**2
print('The area of the circle with radius', radius, 'is:', area, 'sq units')  

#TASK 2
print('TASK 2')
filename = input('Enter file name:')
extension = filename.split('.')
print('extension of the file is:',extension[1])
