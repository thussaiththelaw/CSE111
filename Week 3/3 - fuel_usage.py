#Zak Law
#Get inputs from user to calculate mpg and liters per 100 kilometers using functions
def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = int(input('What is the beginning odometer reading?: '))
    # Get another odometer value in U.S. miles from the user.
    end_miles = int(input('What is the ending odometer reading?: '))
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input('How many gallons were used?: '))
    #call the miles per gallon function to get mpg variable
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    #call liters per 100 kilometers funtion to get a lp100k variable
    lp100k = lp100k_from_mpg(mpg)

    #print miles per gallon to 1 decimal place
    print(f'{mpg:.1f} miles per gallon')
    #print liters per 100 kilometers to 2 decimal places
    print(f'{lp100k:.2f} liters per 100 kilometers')
    pass

#Miles per gallon function
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    #miles per gallon is miles traveled divided by the gallons of fuel used
    mpg = (end_miles - start_miles)/amount_gallons
    return mpg

#liters per 100 kilomaters function
def lp100k_from_mpg(mpg):
    #convert miles per gallon to liters per 100 kilometers
    lp100k = 235.215 / mpg
    #return lp100k to the function
    return lp100k


# Call the main function so that
# this program will start executing.
main()