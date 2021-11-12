#Zak Law
#Written 9/29/2021

#Import datetime for age calculation
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('What is your gender?(M or F): ')
    birth = input('What is your birthday?(YYYY-MM-DD): ')
    weight_lb = int(input('What is your weight in pounds?: '))
    height_in = int(input('What is your height in inches?: '))

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.

    print(f'Age: {compute_age(birth)}')
    print(f'Weight (kg): {kg_from_lb(weight_lb):.1f}')
    print(f'Height (cm): {cm_from_in(height_in):.1f}')
    print(f'Body mass index: {body_mass_index(weight_lb, height_in):.1f}')
    print(f'Basal metabolic rate: {basal_metabolic_rate(gender, birth, weight_lb, height_in):.0f}')


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    age = years
    return age


def kg_from_lb(weight_lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    weight_kg = weight_lb * 0.45359237
    return weight_kg


def cm_from_in(height_in):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    height_cm = height_in * 2.54
    return height_cm


def body_mass_index(weight_lb, height_in):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    weight_kg = kg_from_lb(weight_lb)
    height_cm = cm_from_in(height_in)
    bmi = (10000 * weight_kg) / (height_cm ** 2)
    return bmi


def basal_metabolic_rate(gender, birth, weight_lb, height_in):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    weight_kg = float(kg_from_lb(weight_lb))
    height_cm = float(cm_from_in(height_in))
    age = int(compute_age(birth))
    if gender.lower() == 'f':
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    elif gender.lower() == 'm':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    return bmr


# Call the main function so that
# this program will start executing.
main()