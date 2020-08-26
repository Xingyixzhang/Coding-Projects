""" This Python application supports voter registration in the command line prompt. """

# Import sys to use sys.exit() function.
import sys

print('Welcome to the Python Voter Registration Application!',
      'Please note that to make a valid registration, all fields must be entered.')

# Prompt the user for their first name and ensure the field is not empty.
firstname = input('Please enter your First Name:\t')
while firstname == '':
    firstname = input('This field is required, please enter your First Name:\t')

# Prompt the user for their last name and ensure the field is not empty.
lastname = input('Please enter your Last Name:\t')
while lastname == '':
    lastname = input('This field is required, please enter your Last Name:\t')

# Prompt the user for their age and ensure the value is valid.
age = int(input('Please enter your age as an integer: '))
while age < 18 or age > 120:
    print('Sorry, you are not eligiable to vote. Please close the registration')
    age = int(input('If this is a mistake, please enter your age again (18 - 120):'))

# Prompt the user to validate their citizenship.
citizenship = input('Are you a U.S. Citizen? (Y/N)')
if citizenship == 'N':
    print('Sorry, you are not eligiable to vote. Please close the registration.')

# If the user is eligible, ask if they are willing to continue.
cont = input('Do you want to continue with the voter registration? (yes/no) ')
if cont == 'no':
    print('Okay, have a nice day!')
    sys.exit()

# Make a list of US states in abbreviation.
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Prompt the user for their state of residency and validate the state abbreviation.
state = input('What state do you live in? (please enter the 2-letter representation) ')
while state not in states:
    state = input('Sorry, the state you entered is invalid, please try again: ')
    cont = input('Do you want to continue with the voter registration? (yes/no) ')
    if cont == 'no':
        print('Okay, have a nice day!')
        sys.exit()

# Prompt the user for their zip code and ensure the field is not empty.
zipcode = input('Please enter your zip code: ')
while zipcode == '':
    zipcode = input('This field is required, please enter your zipcode:\t')

# Sum up the information gathered.
print('\nThank you for registering to vote!',
      'Here is the information we have received from you:')

print(f'\nName: {firstname} {lastname}')
print(f'Age: {age}\nU.S. Citizen: {citizenship}')
print(f'State: {state}\nZip Code: {zipcode}\n')

print('Thanks for trying the Voter Registration Application.',
      'Your voter registration card should be shipped within 3 weeks.')
