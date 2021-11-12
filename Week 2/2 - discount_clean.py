from datetime import datetime as date

#global variables to be used by functions
subtotal = float(0)
discount = float(0)
sales_tax = float(0)
total = float(0)

#functions
def discount_on_subtotal(): #function that multiplies the total by .9 to get 10% off the total price
    global subtotal
    global discount
    discount = subtotal * .1
    sales_tax_and_total() #move on to calculate sales tax on discounted total

def sales_tax_and_total(): #calculates 
    global subtotal
    global sales_tax
    global total
    sales_tax = (subtotal * .06)
    total = ((subtotal - discount) + sales_tax)

day = date.today().strftime("%A") #get the day (ex. 'Monday' or 'Tuesday' or 'Wednesday'...)
print (day)
discount_day = None
if (day == 'Tuesday') or (day == 'Wednesday'): #if the current day is Tuesday or Wednesday
    discount_day = True #set the discount variable to True
#     print ('discount = true')
# else:
#     print ('dicount = false')

checkout = True
while checkout == True: #loop to get price and quantity until the user types "0"
    price = float(input('How much is the item? (type "0" to end): '))
    if price == 0:
        break
    else:
        quantity = int(input('How many would you like to purchase?: '))
        subtotal = subtotal + (price * quantity)

if discount_day == True: #if it is Tuesday or Wednesday
    if subtotal >= 50: #and the subototal is equal to or greater than $50
        discount_on_subtotal() #give the discount, and go through the rest of the funtions to calculate the total sale
        print (f'Because it is {day} you get a 10% discount off your purchase of ${subtotal:.2f}, which comes out to {total:.2f} with an included sales tax of ${sales_tax:.2f}.')
    else: #tell the user the remaining purchase amount to get the discount
        purchase_more = 50 - subtotal
        print (f'To get a %10 discount off of your purchase, you need to buy ${purchase_more:.2f} worth of additional items.')
        sales_tax_and_total() # go through the functions without the discount
        print (f'Your total comes out to be ${total:.2f}, with a sales tax of ${sales_tax:.2f} included.')
else: #if it isn't a discount day
    sales_tax_and_total() #go through the functions without the discount
    print (f'Your total comes out to be ${total:.2f}, with a sales tax of ${sales_tax:.2f} included.')