#Zak Law
#This program takes information from the tire volume data and stores it onto a txt file along with date and time information
from datetime import datetime
import math

def tire_volume(): #gets measurment input from the user, and feeds the information to the tire_information_collection function
    #input from user
    print ('Please type the following values:')
    width = float(input('Width(in millimeters): '))
    aspect_ratio = float(input('Aspect Ratio: '))
    diameter = float(input('Diameter (in inches)'))
    volume = ((math.pi * width**2 * aspect_ratio * ((width * aspect_ratio + (2540 * diameter)))) / 10000000000)
    print (f'The approximate volume of the tire is {volume:.2f} liters')
    purchase_tires = input('Would you like to buy tires in that size?(YES or NO): ')
    tire_information_collection(width, aspect_ratio, diameter, volume, purchase_tires)

def tire_information_collection(width, aspect_ratio, diameter, volume, purchase_tires):
    open ('volumes.txt')
    current_date_and_time = datetime.now()
    if purchase_tires.lower() == 'yes':
        phone_number = input('What is your phone number?(ex. 456-234-6789): ')
        with open('volumes.txt', 'at') as dimens_file:
            print(f'{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number}', file=dimens_file)
    else:
        with open('volumes.txt', 'at') as dimens_file:
            print(f'{current_date_and_time:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}', file=dimens_file)

tire_volume()