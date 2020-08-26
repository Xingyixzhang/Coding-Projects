"""This command line app allows users to perform math and security related functions."""
import sys
import math
import random
import string
from datetime import date

print('\nWelcome to the functions!')

def generate_menu():
    """Generate the menu for user choice."""
    print('\nPlease choose from the following menu:',
          '\n\na. Generate Secure Password.',
          '\nb. Calculate and Format a Percentage.',
          '\nc. How many days from today until July 4, 2025?',
          '\nd. Use the Law of Cosines to calculate the leg of a triangle.',
          '\ne. Calculate the volumn of a Right Circular Cylinder.',
          '\nf. Exit the program.')

def generate_password(uppercase, lowercase, num, special_char):
    """Generate Secure Password with the user-defined length."""

    # Create a list of characters based on user request for each type:
    char_list = ''.join((random.choice(string.ascii_uppercase) for i in range(uppercase)))
    char_list += ''.join((random.choice(string.ascii_lowercase) for i in range(lowercase)))
    char_list += ''.join((random.choice(string.digits) for i in range(num)))
    char_list += ''.join((random.choice(string.punctuation) for i in range(special_char)))

    # Shuffle the list of characters so they are more random to enhance the password security:
    shuffled_list = list(char_list)
    random.shuffle(shuffled_list)

    # Join the shuffled character list into the final password string, then print out for user:
    password = ''.join(shuffled_list)

    print(f'\nHere is your auto-generated password: {password}')

def calculate_format_perc(num, denom, dec):
    """Calculate and format a percentage based on the user input values."""
    percent = num / denom
    print(f'\nThe percentage of your question is: {percent:.{dec}f}')

def count_days():
    """Count the days from today til July 4, 2025."""
    today = date.today()
    end_date = date(2025, 7, 4)
    days_away = abs(end_date - today)
    print(f'You have {days_away.days} more days until July 4, 2025.')

def calculate_triangle_leg(a_side=8, b_side=11, c_angle=37):
    """Calculate the leg of a triangle using the law of Cosines. (default params used)"""

    # Calculate the radians for angel C, then use the formular to calculate the leg:
    rad = math.radians(c_angle)
    c_side = math.sqrt(a_side**2 + b_side**2 - 2*a_side*b_side*math.cos(rad))

    print(f'For your triangle with a = {a_side}, b = {b_side},',
          f'angle C is {c_angle} degree -- the length of leg c is: {c_side:.2f}')

def calculate_volumn(radius, height):
    """Calculate the volumn of a right circular cylinder."""
    vol = math.pi * radius**2 * height
    print(f'\nThank you for the data, the volumn of your right cylinder is: {vol:.2f}')

def exit_program():
    """Thank the user for visiting the application and exit the program."""
    print('Thank you for visiting our program, see you next time!',
          '\nExiting the program ...')
    sys.exit()

def take_action(choice):
    """Validate user input and give retries, then determine which funtion to invoke."""
    if choice.lower() == 'a':
        print('\nHow long do you want the password to be?',
              'Please keep that in mind when answering the following complexity questions:')

        # Prompt the user to enter their specific requests based on the length of password:
        uppercase = int(input('\nHow many uppercase letter would you like to include? '))
        lowercase = int(input('How many lowercase letter would you like to include? '))
        number = int(input('How many numbers would you like to include? '))
        special = int(input('How many special characters would you like to include? '))

        # Call the function to generate the secure password:
        generate_password(uppercase, lowercase, number, special)
    elif choice.lower() == 'b':
        # Prompt the user for values they want to perform calculation with:
        num = float(input('Please enter a numerator: '))
        denom = float(input('Please enter a denominator: '))
        dec = int(input('Please enter the number of decimal points for your formatting: '))

        # Validate user input for number of decimal point:
        while dec < 0:
            dec = int(input('Negative input, please re-enter the decimal point number: '))

        calculate_format_perc(num, denom, dec)
    elif choice.lower() == 'c':
        # No user input required, call the function directly to count days:
        count_days()
    elif choice.lower() == 'd':
        # Call the function with default parameters, no need for user input in this case:
        calculate_triangle_leg()
    elif choice.lower() == 'e':
        # Prompt and validate the user for the radius and height of the right cylinder:
        radius = float(input('\nPlease enter the radius of the cylinder base: '))
        while radius < 0:
            radius = float(input('\nNegative value, please re-enter the radius: '))

        height = float(input('Please enter the height of your right cylinder: '))
        while height < 0:
            height = float(input('\nNegative value, please re-enter the height: '))

        # Call the function to perform calculation:
        calculate_volumn(radius, height)
    elif choice.lower() == 'f':
        exit_program()
    else:
        # Validate the user input and provide retry/quit opportunities:
        cont = input('Invalid input, do you want to retry to continue? (y/n)').lower()
        if cont == 'y':
            choice = input('\nWhich function would you love to invoke? ')
            take_action(choice)
        else:
            exit_program()

# Call the functions to run the application:
generate_menu()
user_choice = input('\nWhich function would you love to invoke? ')
take_action(user_choice)
