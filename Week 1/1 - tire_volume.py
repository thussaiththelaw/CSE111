#This program uses input from the user to calculate the volume in a tire
#Zak Law

import math

#input from user
print ('Please type the following values:')
width = float(input('Width(in millimeters): '))
aspect_ratio = float(input('Aspect Ratio: '))
diameter = float(input('Diameter (in inches)'))

#math
volume = ((math.pi * width**2 * aspect_ratio * ((width * aspect_ratio + (2540 * diameter)))) / 10000000000)

#output
print (f'The approximate volume of the tire is {volume:.2f} liters')