"""This matrix game performs matrix operations using NumPy and Pandas functionality."""
import re
import numpy

# Welcome the user to play the Python matrix game:
print('*'*20, 'Welcome to the Python Matrix Application', '*'*20)

def confirm_play():
    """Confirm whether the user would like to play the game."""
    response = input('\nDo you want to play the Matrix Game? (y/n) ').lower()

    while response not in ('y', 'n'):
        response = input('Invalid response, would you like to play the game? (y/n) ').lower()

    if response == 'y':
        run_application()

    if response == 'n':
        exit_program()

def phone_number():
    """Prompt the user for their phone number and validate the input."""
    user_input = input('\nPlease enter your phone number (Digit Only): ')

    # Validate the value type and length of user input:
    while True:
        try:
            int(user_input)
            if len(user_input) != 10:
                user_input = input('Invalid length, please reenter your phone number: ')
                continue
            break
        except ValueError:
            user_input = input('Invalid value, please enter your phone number (Digit Only): ')

    # Format the phone number using regular expression pattern:
    pattern = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', user_input)
    formatted_number = '-'.join(pattern.groups())

    # Another way to format the phone number:
    # formatted_number = format(int(user_input[:-1]), ",").replace(",", "-") + user_input[-1]

    return formatted_number

def zip_code():
    """Prompt the user for their zipcode and validate the input."""
    user_input = input('\nPlease enter your zip code+4 (XXXXX-XXXX): ')

    # Validate the value and format of user input:
    while True:
        if len(user_input) != 10:
            user_input = input('Invalid lenth, please re-enter (XXXXX-XXXX): ')
        if user_input[:5].isdigit() and user_input[6:].isdigit():
            if user_input[5] == '-':
                break
            user_input = input('Invalid format, please re-enter (XXXXX-XXXX): ')
        else:
            user_input = input('Invalid zipcode numbers, please re-enter (XXXXX-XXXX): ')

    return user_input

def validate_matrix(user_matrix):
    """Validate the user input (format and value type)."""
    number_set = user_matrix.split()
    number_together = user_matrix.replace(' ', '')

    while True:
        if len(number_set) != 9:
            response = input('\nInvalid length, please enter a 9-digit matrix: ')
        elif not number_together.isdigit():
            response = input('\nInvalid number(s), please re-enter your matrix: ')
        else:
            # format matrix in a 3x3 multiD array:
            formatted_matrix = numpy.array(number_set).reshape(3, 3)
            return formatted_matrix

        number_set = response.split()
        number_together = response.replace(' ', '')

def display_matrix(user_matrix):
    """Display the matrix in a table format."""
    for row in range(3):
        cols = user_matrix[row]

        for col in cols:
            print(f'{col:<6}', end=' ')

        # create a new line after each row of numbers:
        print()

def generate_ops():
    """Generate matrix operations list for user choice."""
    print('\nSelect a Matrix Operation from the list below:',
          '\na. Addition',
          '\nb. Subtraction',
          '\nc. Matrix Multiplication',
          '\nd. Element-by-Element Multiplication')
    return input()

def add_matrix(matrix1, matrix2):
    """Perform Matrix addition operation."""
    return numpy.add(matrix1, matrix2)

def subtract_matrix(matrix1, matrix2):
    """Perform Matrix subtraction operation."""
    return numpy.subtract(matrix1, matrix2)

def multiply_matrix(matrix1, matrix2):
    """Perform Matrix multiplication operation."""
    return numpy.matmul(matrix1, matrix2)

def multiply_ele(matrix1, matrix2):
    """Perform element-by-element operations for both matrix."""
    return numpy.multiply(matrix1, matrix2)

def display_result(operation_name, result):
    """Display the results for operations chosen by the user."""
    print(f'\nYou have selected {operation_name}. The result is:')
    display_matrix(result)

def display_transpose(result):
    """Display the transpose of operation result from the matrices."""
    print('\nThe transpose of the result is:')
    transpose = result.T
    display_matrix(transpose)

def display_mean(result):
    """Display the mean value for the rows and columns in result matrix."""
    print('\nThe mean values of result matrix\'s rows and columns are:')

    # Calculate the mean values of each row and column of the result matrix:
    row1 = numpy.mean(result[0])
    row2 = numpy.mean(result[1])
    row3 = numpy.mean(result[2])

    col1 = numpy.mean(result[:, 0])
    col2 = numpy.mean(result[:, 1])
    col3 = numpy.mean(result[:, 2])

    # Display the values:
    print(f'First Row: {row1:<6}\tFirst Column: {col1}')
    print(f'Second Row: {row2:<6}\tSecond Column: {col2}')
    print(f'Third Row: {row3:<6}\tThird Column: {col3}')

def take_action(choice, matrix1, matrix2):
    """Run selected operation based on the user choice."""

    # Set the type of two ndarray matrices to float value for math operations:
    matrix1 = numpy.array(matrix1, dtype=float)
    matrix2 = numpy.array(matrix2, dtype=float)
    result = numpy.array([], dtype=float)

    if choice == 'a':
        result = add_matrix(matrix1, matrix2)
        display_result('Addition', result)
        display_transpose(result)
        display_mean(result)
    elif choice == 'b':
        result = subtract_matrix(matrix1, matrix2)
        display_result('Substraction', result)
        display_transpose(result)
        display_mean(result)
    elif choice == 'c':
        result = multiply_matrix(matrix1, matrix2)
        display_result('Matrix Multiplication', result)
        display_transpose(result)
        display_mean(result)
    elif choice == 'd':
        result = multiply_ele(matrix1, matrix2)
        display_result('Matrix Multiplication by Element', result)
        display_transpose(result)
        display_mean(result)
    else:
        # Validate the user input and provide retry/quit opportunities:
        cont = input('Invalid input, do you want to retry to continue? (y/n)').lower()

        while cont not in ('y', 'n'):
            cont = input('Invalid response, would you like to try again? (y/n) ').lower()

        if cont == 'y':
            choice = input('\nWhich one wold you like to proceed with? ')
            take_action(choice, matrix1, matrix2)

def run_application():
    """Operations flow of the whole application."""

    # Prompt the user for their phone number and zipcode with input validation methods:
    phone_str = phone_number()
    print(f'Thank you! Here is your confirmed phone number: {phone_str}')

    zipcode = zip_code()
    print(f'Thank you! Here is your confirmed zipcode: {zipcode}')

    # Prompt the user for their matrix number sets, validate the user input:
    first_input = input('\nPlease enter your first 3x3 matrix: (separate by a space) ')
    first_matrix = validate_matrix(first_input)

    second_input = input('\nPlease enter your second 3x3 matrix: (separate by a space) ')
    second_matrix = validate_matrix(second_input)

    # Display both formatted matrix:
    print('\nHere are your matrix sets:')
    print('\nFirst Matrix:')
    display_matrix(first_matrix)
    print('\nSecond Matrix:')
    display_matrix(second_matrix)

    # Generate a list of matrix operations and perform action based on user choice:
    user_choice = generate_ops()
    take_action(user_choice, first_matrix, second_matrix)

    # To confirm if the user would love to continue playing:
    confirm_play()

def exit_program():
    """Thank the user for playing the game and exit the program gracefully."""
    print('\nExiting the program ...')
    print()
    print('*'*20, 'Thanks for playing Python Matrix', '*'*20)

confirm_play()
