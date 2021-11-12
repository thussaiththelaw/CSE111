#Zak Law
#This program gets two inputs from a user, items, items per box, and returns how many boxes they will need

import math

#inputs from user; items needed to pack, and how many items can be packed in a box
items = int(input('How many items do you have? '))
pack = int(input('How many items can you fit in a box? '))

#math; divide items by items able to fit in a box, and round up to the nearest whole number.
boxes = math.ceil(items / pack)

#display inputs, and the boxes needed to pack the items
print (f'For {items} items, packing {pack} items in each box, you will need {boxes} boxes')