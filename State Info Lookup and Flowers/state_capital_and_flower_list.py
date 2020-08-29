"""This app allows users with the to search and display US State Capital, population and Flowers."""
import matplotlib.pyplot as plt # graphing capabilities
import matplotlib.image as mpimg
import seaborn as sns

print('\nWelcome to the States and Flowers list!')

def generate_menu():
    """Generate the menu for user choice."""
    print('\nPlease choose from the following menu:',

          '\n\n1. Display all U.S. States in Alphabetical order along',
          'with the Capital, State Population, and Flower',

          '\n2. Search for a specific state and display the appropriate Capital',
          'name, State Population, and an image of the associated State Flower.',

          '\n3. Provide a Bar graph of the top 5 populated States showing the overall population.',

          '\n4. Update the overall state population for a specific state.',

          '\n5. Exit the program.')

# Make a list of US States' Abbriviations:
state_abbr_dict = {
    "AL": "Alabama",
    "AK":"Alaska",
    "AZ":"Arizona",
    "AR":"Arkansas",
    "CA":"California",
    "CO":"Colorado",
    "CT":"Connecticut",
    "DE":"Delaware",
    "FL":"Florida",
    "GA":"Georgia",
    "HI":"Hawaii",
    "ID":"Idaho",
    "IL":"Illinois",
    "IN":"Indiana",
    "IA":"Iowa",
    "KS":"Kansas",
    "KY":"Kentucky",
    "LA":"Louisiana",
    "ME":"Maine",
    "MD":"Maryland",
    "MA":"Massachusetts",
    "MI":"Michigan",
    "MN":"Minnesota",
    "MS":"Mississippi",
    "MO":"Missouri",
    "MT":"Montana",
    "NE":"Nebraska",
    "NV":"Nevada",
    "NH":"New Hampshire",
    "NJ":"New Jersey",
    "NM":"New Mexico",
    "NY":"New York",
    "NC":"North Carolina",
    "ND":"North Dakota",
    "OH":"Ohio",
    "OK":"Oklahoma",
    "OR":"Oregon",
    "PA":"Pennsylvania",
    "RI":"Rhode Island",
    "SC":"South Carolina",
    "SD":"South Dakota",
    "TN":"Tennessee",
    "TX":"Texas",
    "UT":"Utah",
    "VT":"Vermont",
    "VA":"Virginia",
    "WA":"Washington",
    "WV":"West Virginia",
    "WI":"Wisconsin",
    "WY":"Wyoming"
}

# Make a dictionary of State information set inc. capital, population, and flower.
state_info_dict = {
    'Alabama': ['Montgomery', 4908620, 'Camelia'],
    'Alaska': ['Juneau', 734002, 'Alpine Forget-me-not'],
    'Arizona': ['Phoenix', 7378490, 'Saguaro Cactus Blossom'],
    'Arkansas': ['Little Rock', 3039000, 'Apple Blossom'],
    'California': ['Sacramento', 39937500, 'California Poppy'],
    'Colorado': ['Denver', 5845530, 'White and Lavender Columbine'],
    'Connecticut': ['Hartford', 3563080, 'Mountain Laurel'],
    'Delaware': ['Dover', 982895, 'Peach Blossom'],
    'Florida': ['Tallahassee', 21993000, 'Orange Blossom'],
    'Georgia': ['Atlanta', 10736100, 'Cherokee Rose'],
    'Hawaii': ['Honolulu', 1412690, 'Hibiscus'],
    'Idaho': ['Boise', 1826160, 'Syringa'],
    'Illinois': ['Springfield', 12659700, 'Purple Violet'],
    'Indiana': ['Indianapolis', 6745350, 'Peony'],
    'Iowa': ['Des Moines', 3179850, 'Wild Prairie Rose'],
    'Kansas': ['Topeka', 2910360, 'Sunflower'],
    'Kentucky': ['Frankfort', 4499690, 'Goldenrod'],
    'Louisiana': ['Baton Rouge', 4645180, 'Magnolia'],
    'Maine': ['Augusta', 1345790, 'White Pine Cone and Tassel'],
    'Maryland': ['Annapolis', 6083120, 'Black-Eyed Susan'],
    'Massachusetts': ['Boston', 6976600, 'Mayflower'],
    'Michigan': ['Lansing', 10045000, 'Apple Blossom'],
    'Minnesota': ['Saint Paul', 5700670, 'Pink and White Lady Slipper'],
    'Mississippi': ['Jackson', 2989260, 'Magnolia'],
    'Missouri': ['Jefferson City', 6169270, 'White Hawthorn Blossom'],
    'Montana': ['Helena', 1086760, 'Bitterroot'],
    'Nebraska': ['Lincoln', 1952570, 'Goldenrod'],
    'Nevada': ['Carson City', 3139660, 'Sagebrush'],
    'New Hampshire': ['Concord', 1371250, 'Purple Lilac'],
    'New Jersey': ['Trenton', 8936570, 'Violet'],
    'New Mexico': ['Santa Fe', 2096640, 'Yucca Flower'],
    'New York': ['Albany', 19440500, 'Rose'],
    'North Carolina': ['Raleigh', 10611900, 'Dogwood'],
    'Ohio': ['Columbus', 11747700, 'Scarlet Carnation'],
    'Oklahoma': ['Oklahoma City', 3954820, 'Mistletoe'],
    'Oregon': ['Salem', 4301090, 'Oregon Grape'],
    'Pennsylvania': ['Harrisburg', 12820900, 'Mountain Laurel'],
    'Rhode Island': ['Providence', 1056160, 'Violet'],
    'South Carolina': ['Columbia', 5210100, 'Yellow Jessamine'],
    'North Dakota': ['Bismarck', 761723, 'Wild Prairie Rose'],
    'South Dakota': ['Pierre', 903027, 'Pasque Flower'],
    'Tennessee': ['Nashville', 6897580, 'Iris'],
    'Texas': ['Austin', 29472300, 'Bluebonnet'],
    'Utah': ['Salt Lake City', 3282120, 'Sego Lily'],
    'Vermont': ['Montpelier', 628061, 'Red Clover'],
    'Virginia': ['Richmond', 8626210, 'Dogwood'],
    'Washington': ['Olympia', 7797100, 'Pink Rhododendron'],
    'West Virginia': ['Charleston', 1778070, 'Rhododendron'],
    'Wisconsin': ['Madison', 5851750, 'Wood Violet'],
    'Wyoming': ['Cheyenne', 567025, 'Indian Paintbrush']
}

def convert_to_abbr(state):
    """Reverse check the abbriviation of a State."""
    for key, val in state_abbr_dict.items():
        if val == state:
            return key
    return None

def display():
    """Display all States in order and their capitals, population, and flower."""

    print(f'\n{"State":<20}{"Capital":<20}{"Population":<20}{"Flower":<20}')
    print()
    for state in sorted(state_info_dict):
        info_list = state_info_dict[state]
        capital = info_list[0]
        population = f'{info_list[1]:,}'
        flower = info_list[2]
        print(f'{state:<20}{capital:<20}{population:<20}{flower:<20}')

def search_state(state):
    """Search for a state and display its capital, population, and State flower image."""

    # Assign information to variables accordingly:
    capital, population, flower = state_info_dict[state]

    # Display related information for the specified State:
    print(f'\nHere are the information for {state}:',
          f'\n\nState Capital: {capital}',
          f'\nState Population: {population:,}',
          f'\nState Flower: {flower}')

    # Display the State flower image:
    state_abbr = convert_to_abbr(state)
    img = mpimg.imread(f'Lab3 Flower Set\\{state_abbr}.jpg')

    plt.imshow(img)
    plt.title(f'{flower}')
    plt.show()

def draw_bar_graph():
    """Show a bar graph of the top 5 populated States and their overall population."""

    # Order the States info list by the State population and get the top 5:
    sorted_states = sorted(state_info_dict.items(), key=lambda x: x[1][1], reverse=True)
    top_5 = sorted_states[:5]

    # Make lists for the top 5 states and their population:
    states = []
    population = []
    for state in top_5:
        states.append(state[0])
        population.append(int(state[1][1]))

    # Graph the bar presentation:
    axes = sns.barplot(x=states, y=population, palette='bright')
    axes.set_title('Top 5 populated States in US')
    axes.set(xlabel='States', ylabel='Population')

    # Leave proper amount of blank space on top of the highest bar:
    axes.set_ylim(top=max(population) * 1.10)

    # Format the texts and their positions in the bar graph:
    for rep, population in zip(axes.patches, population):
        text_x = rep.get_x() + rep.get_width() / 2.0
        text_y = rep.get_height()
        text = f'{population:,}'
        axes.text(text_x, text_y, text,
                  fontsize=11, ha='center', va='bottom')

    # Display the bar graph:
    plt.show()

def update_population(state):
    """Update the overall population for a specific State"""
    state_info = state_info_dict[state]
    old_population = state_info[1]
    print(f'{state} currently has the population of: {old_population:,}.')

    # Prompt the user for a new population and validate it:
    new_population_str = input(f'Please enter the updated population for {state}: ')
    new_population = validate_population(new_population_str)
    state_info[1] = new_population

    # Ask the user to check list, or continue with next operation, or exit the program:
    cont = input('\nThank you for the update, would you like to check the list? (y/n) ').lower()
    if cont == 'y':
        display()
    choose_next()

def exit_program():
    """Thank the user for visiting the application and exit the program."""
    print('Thank you for visiting our program, see you next time!',
          '\nExiting the program ...')

def validate_state():
    """Validate the State user entered, prompt error and retry message when invalid."""
    state = input('Please enter a State: ')
    while True:
        for key, val in state_abbr_dict.items():
            if state in (key, val):
                return val
        state = input('Invalid input, please enter a State: (i.e. \"AL\" or \"Alabama\") ')

def validate_population(pop):
    """Validate is the user input represents a valid State population"""
    valid_number = False
    while not valid_number:
        try:
            new_pop = int(pop)
            if new_pop > 0:
                valid_number = True
            else:
                pop = input('Not a positive value for the State population, please try again: ')
        except ValueError:
            pop = input('Invalid number, please enter a valid number for population update: ')
    return new_pop

def choose_next():
    """Prompt user to continue with next choice or exit."""
    cont = input('\nWould you like to make another choice? (y/n) ').lower()

    while cont not in ('y', 'n'):
        cont = input('Invalid response, would you like to try again? (y/n) ').lower()

    if cont == 'y':
        run_application()
    else:
        exit_program()

def take_action(choice):
    """Validate user inputs, allow retries, and invoke function accordingly."""
    if choice == '1':
        display()
        choose_next()
    elif choice == '2':
        state = validate_state()
        search_state(state)
        choose_next()
    elif choice == '3':
        draw_bar_graph()
        choose_next()
    elif choice == '4':
        state = validate_state()
        update_population(state)
    elif choice == '5':
        exit_program()
    else:
        # Validate the user input and provide retry/quit opportunities:
        cont = input('Invalid input, do you want to retry to continue? (y/n)').lower()

        while cont not in ('y', 'n'):
            cont = input('Invalid response, would you like to try again? (y/n) ').lower()

        if cont == 'y':
            choice = input('\nWhich one wold you like to proceed with? ')
            take_action(choice)
        else:
            exit_program()

def run_application():
    """Call the functions to run the application."""
    generate_menu()
    choice = input('\nWhich one wold you like to proceed with? ')
    take_action(choice)

run_application()
