# Name: Kyle Cortez

# Use these commands to change the state of the game. Prompts will give an indication of next input expected
# Commands ~should~ not care of capitalization. nOrTh is perfectly acceptable as an input, albeit weird.
def command_list():
    command = ['Move', 'Wait', 'Exit', 'Quit']
    return command


# Todo Bug with 'Wait' state being unable to remove wait as a command. Redo logic or to accept list
# Note: Allows an extra list of commands to allow something like exiting at any time an option.
def validate_input(command_dict, optional=None, remove_commands=None):
    if optional is not None:
        optional.remove(remove_commands)
    if optional is None:
        optional = []

    command = input().title()
    while command not in command_dict:
        if command in optional:
            break
        command = input("Invalid input, try another\n").title()
    # print(direction)
    return command


def yn_validate():
    string = input('Y/N?\n').lower()
    while string != 'y' and string != 'n' and string != 'yes' and string != 'no':
        print('Invalid input: Y/N')
        string = input().lower()
    return string[0]


def move_room(direction, current_location, rooms_dict):
    return rooms_dict.get(current_location).get(direction)


def direction_list(cardinals):
    cardinals = str(cardinals)
    cardinals = cardinals[cardinals.index('[') + 1: cardinals.index(']')]
    return cardinals.replace("'", '').title()


if __name__ == '__main__':

    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

    commands = command_list()
    print(commands)
    default_command = 'Wait'
    starting_room = 'Bedroom'

    current_room = starting_room
    current_command = default_command
    running = False

    print("Initiate?")
    if yn_validate() == 'y':
        print('Initiated')
        running = True
    else:
        running = True
        current_command = 'Exit'

    while running:
        while current_command == 'Wait':
            print('Current location is: {}'.format(current_room.title()))
            print('Awaiting a command.')
            print(commands)
            current_command = validate_input(commands)

        while current_command == 'Move':
            directions = rooms.get(current_room).keys()
            print('What direction?')
            print('You have doors to the: {}'.format(direction_list(directions)))
            current_direction = validate_input(rooms.get(current_room), commands.copy(), current_command)
            if current_direction not in rooms.get(current_room):
                current_command = current_direction
                break
            current_room = move_room(current_direction, current_room, rooms)

            print('Moved to {}'.format(current_room.title()))
            current_command = default_command

        # Added the alternate quit because I kept typing it and invalidating input.
        while current_command == 'Exit' or current_command == 'Quit':
            print('Are you sure you want to exit?')
            if yn_validate() == 'n':
                current_command = default_command
                break
            exit('Exited game')
