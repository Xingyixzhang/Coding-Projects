"""This app loads CSV file, runs histogram analysis, and plots variables on the datasets."""
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

# Welcome the user to the data analysis application:
print('*'*20, 'Welcome to the Python Data Analysis App', '*'*20)

# Store columns of each data file into two lists:
population_cols = ["Pop Apr 1", "Pop Jul 1", "Change Pop"]
housing_cols = ["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]

# Format the .describe() output to 2 decimal points:
pd.set_option('display.float_format', lambda x: '%.2f' % x)

def user_input():
    """Generate available files and get the user choice."""
    print('\nSelect the file you would like to analyze:',
          '\n1. Population Data',
          '\n2. Housing Data',
          '\n3. Exit the Program')
    return input()

def get_pop_column():
    """Display columns in the Population File for user choice to analyze."""
    print('\nPlease select the column to analyze:',
          f'\na. {population_cols[0]}',
          f'\nb. {population_cols[1]}',
          f'\nc. {population_cols[2]}',
          '\nd. Exit Column')
    return input()

def get_hou_column():
    """Display columns available in the Housing File for user to analyze."""
    print('\nPlease select the column to analyze:',
          f'\n1. {housing_cols[0]:<10}', f'2. {housing_cols[1]:<20}',
          f'3. {housing_cols[2]:<10}', f'\n4. {housing_cols[3]:<10}',
          f'5. {housing_cols[4]:<20}', '6. Exit Column')
    return input()

def show_continue(colselected):
    """Show the plot and continue to prompt for next user choice."""
    plt.show()
    print(colselected.describe())

    table_choice = user_input()
    take_action(table_choice)

def take_pop_action(choice):
    """Run appropriate analysis based on the population data column chosen by user."""
    popfile = pd.read_csv('PopChange.csv')
    if choice == 'a':
        print(f'\nYou have selected \"{population_cols[0]}\"',
              'Here are the statistics for this column:')
        colselected = popfile[population_cols[0]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('Pop Apr 1\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == 'b':
        print(f'\nYou have selected \"{population_cols[1]}\"',
              'Here are the statistics for this column:')
        colselected = popfile[population_cols[1]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('Pop Jul 1\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == 'c':
        print(f'\nYou have selected \"{population_cols[2]}\"',
              'Here are the statistics for this column:')
        colselected = popfile[population_cols[2]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('Change Pop\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == 'd':
        print('You have exited the columns.')
        table_choice = user_input()
        take_action(table_choice)
    else:
        # Validate the user input and provide retry/exit opportunities:
        cont = input('Invalid choice, do you want to retry to continue? (y/n)').lower()

        while cont not in ('y', 'n'):
            cont = input('Invalid input, would you like to try again? (y/n) ').lower()

        if cont == 'y':
            col_chosen = get_pop_column()
            take_pop_action(col_chosen)
        else:
            exit_program()

def take_hou_action(choice):
    """Run appropriate analysis based on the housing data column chosen by user."""
    houfile = pd.read_csv('Housing.csv')

    if choice == '1':
        print(f'\nYou have selected \"{housing_cols[0]}\".',
              'Here are the statistics for this column:')
        colselected = houfile[housing_cols[0]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('AGE\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == '2':
        print(f'\nYou have selected \"{housing_cols[1]}\".',
              'Here are the statistics for this column:')
        colselected = houfile[housing_cols[1]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('BEDROOMs\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == '3':
        print(f'\nYou have selected \"{housing_cols[2]}\".',
              'Here are the statistics for this column:')
        colselected = houfile[housing_cols[2]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('BUILT\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == '4':
        print(f'\nYou have selected \"{housing_cols[3]}\".',
              'Here are the statistics for this column:')
        colselected = houfile[housing_cols[3]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('ROOMs\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == '5':
        print(f'\nYou have selected \"{housing_cols[4]}\".',
              'Here are the statistics for this column:')
        colselected = houfile[housing_cols[4]]
        colselected.hist(figsize=(10, 7), bins=100)
        plt.title('UTILITY\n\n', fontweight='bold')
        show_continue(colselected)
    elif choice == '6':
        print('You have exited the columns.')
        table_choice = user_input()
        take_action(table_choice)
    else:
        # Validate the user input and provide retry/exit opportunities:
        cont = input('Invalid choice, do you want to retry to continue? (y/n)').lower()

        while cont not in ('y', 'n'):
            cont = input('Invalid input, would you like to try again? (y/n) ').lower()

        if cont == 'y':
            col_chosen = get_hou_column()
            take_hou_action(col_chosen)
        else:
            exit_program()

def analyze_population():
    """Ananlyze the Population Data file."""
    print('\nYou have entered the Population Data.')

    popfile = pd.read_csv('PopChange.csv')
    popselected = popfile[population_cols]
    popselected.hist(figsize=(10, 7), bins=100)
    plt.show()
    print(popselected.describe())

    col_chosen = get_pop_column()
    take_pop_action(col_chosen)

def analyze_housing():
    """Analyze the Housing Data file."""
    print('\nYou have entered the Housing Data.')

    housefile = pd.read_csv('Housing.csv')
    houselected = housefile[housing_cols]
    houselected.hist(figsize=(10, 10), bins=50)
    plt.show()
    print(houselected.describe())

    col_chosen = get_hou_column()
    take_hou_action(col_chosen)

def exit_program():
    """Thank the user for using the analysis app and exit the program gracefully."""
    print('\nExiting the program ...')
    print()
    print('*'*20, 'Thanks for using the Data Analysis App', '*'*20)

def take_action(choice):
    """Perform histogram analysis on the chosen file, or exit per user request."""
    if choice == '1':
        analyze_population()
    elif choice == '2':
        analyze_housing()
    elif choice == '3':
        exit_program()
    else:
        # Validate the user input and provide retry/exit opportunities:
        cont = input('Invalid choice, do you want to retry to continue? (y/n)').lower()

        while cont not in ('y', 'n'):
            cont = input('Invalid input, would you like to try again? (y/n) ').lower()

        if cont == 'y':
            choice = input('\nWhich one wold you like to proceed with? ')
            take_action(choice)
        else:
            exit_program()

def run_application():
    """Operations flow of the whole application."""
    choice = user_input()
    take_action(choice)

run_application()
