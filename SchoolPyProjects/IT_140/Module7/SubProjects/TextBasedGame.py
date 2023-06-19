# Name: Kyle Cortez

def instructions():
    return ("Instructions:\n"
            "Move through each of the rooms in search of the 6 artifacts to defeat the villain.\n"
            "Movement is done by declaring the 'move' command, then a cardinal direction.\n"
            "You can search a room for anything of note by using the 'search' command.\n"
            "You can pick up an item by using the 'pickup' command.\n"
            "You can check your inventory at any time by using the 'inventory' command.\n"
            "Use the 'objectives' command to list the current remaining objectives.\n"
            "The 'wait' command can be used to set back to a default state.\n"
            "Commands may be inputted at any time to interrupt another.\n"
            "Type 'exit' or 'quit' to exit at any time.\n")


# Use these commands to change the state of the game. Prompts will give an indication of next input expected
# Commands ~should~ not care of capitalization. nOrTh is perfectly acceptable as an input, albeit weird.
def command_list():
    command = ['move', 'wait', 'exit', 'quit', 'search', 'pickup', 'inventory', 'help', 'objectives']
    return command


# Note: Allows an extra list of commands to allow something like exiting at any time an option.
def validate_input(command_dict, optional=None, remove_commands=None):
    if optional is not None:
        optional.remove(remove_commands)
    if optional is None:
        optional = []

    command = input().lower()
    while command not in command_dict:
        if command in optional:
            break
        if command == 'cheat':
            break
        command = input("Invalid input, try another\n").lower()
    return command


def yn_validate():
    string = input('Y/N?\n').lower()
    while string != 'y' and string != 'n' and string != 'yes' and string != 'no':
        print('Invalid input: Y/N')
        string = input().lower()
    return string[0]


def move_room(direction, current_location, rooms_dict):
    return rooms_dict.get(current_location).get(direction)


def direction_commands(cardinals):
    cardinals = str(cardinals)
    cardinals = cardinals[cardinals.index('[') + 1: cardinals.index(']')]
    return cardinals.replace("'", '').title()


# To print the divider between commands.
def separator():
    print(''.rjust(100, '_'))


def win_check(collection):
    win = True
    for a in collection:
        for b in collection[a]:
            if b in inventory:
                print(f"Attacked with: {str(b).title()} of {str(inventory.get(b)).title()}")
            else:
                win = False
                break
    return win


# For an vs a grammar.
def syllable_check(word):
    vowels = 'aeiou'
    syllable = True

    if vowels.find(word[0]) != -1:
        syllable = False

    return syllable


# For an inline list to a formatted string.
def iterate_value(value):
    string = ''
    for count, a in enumerate(value):
        if count < len(value) - 1:
            string = f"{string}{a}, "
        else:
            string = f"{string}{a}"
    return string


# Had to shorten up the lines to get the whatever of whatever in-line.
def x_of_x_format(collection, value):
    return f"{str(value).title()} of {str(collection.get(value)).title()}"


if __name__ == '__main__':

    rooms = {'tower room': {'north': 'guard quarters'},

             'basement': {'east': 'kitchen'},

             'kitchen': {'north': 'dining room',
                         'south': 'servant quarters',
                         'east': 'guard quarters',
                         'west': 'basement'
                         },

             'sitting room': {'north': 'main hall',
                              'east': 'dining room',
                              'west': 'library'
                              },

             'dining room': {'west': 'sitting room',
                             'south': 'kitchen'
                             },

             'foyer': {'west': 'trophy hall',
                       'south': 'main hall'
                       },

             'library': {'north': 'study',
                         'east': 'sitting room'
                         },

             'study': {'north': 'trophy hall',
                       'south': 'library'
                       },

             'servant quarters': {'north': 'kitchen',
                                  'west': 'living quarters'
                                  },

             'living quarters': {'east': 'servant quarters',
                                 'west': 'garden'
                                 },

             'trophy hall': {'east': 'foyer',
                             'south': 'study'
                             },

             'garden': {'east': 'living quarters'},

             'guard quarters': {'south': 'tower room',
                                'west': 'kitchen'
                                },

             'main hall': {'north': 'foyer',
                           'south': 'sitting room'
                           }
             }

    artifacts = {'kitchen': {'shield': "neh'ctik"},
                 'dining room': {'amulet': "moor gnin'id"},
                 'foyer': {'wristband': "re'yof"},
                 'sitting room': {'icon': "moor gnit'tis"},
                 'study': {'sword': "y'duts"},
                 'library': {'wand': "y'rarb'il"}
                 }

    inventory = {}

    commands = command_list()
    starting_command = 'help'
    default_command = 'wait'
    starting_room = 'tower room'
    # Moved villain room from design doc to better have the player traverse the level.
    villain_room = 'garden'

    current_room = starting_room
    current_command = starting_command
    running = False

    print("Initiate?")
    if yn_validate() == 'y':
        print('Initiated')
        running = True
    else:
        running = True
        current_command = 'exit'

    separator()

    while running:
        # Functions as the default command as the player waits and decides what to do next.
        while current_command == 'wait':
            print(f'Current location is: {current_room.title()}')
            if current_room == villain_room:
                current_command = 'bossfight'
            else:
                print('Awaiting a command.')
                current_command = validate_input(commands)
                separator()

        # You like to move it, move it!
        while current_command == 'move':
            directions = rooms.get(current_room).keys()
            print(f"What direction?\nYou have doors to the: {direction_commands(directions)}.")
            current_direction = validate_input(rooms.get(current_room), commands.copy(), current_command)
            if current_direction not in rooms.get(current_room):
                current_command = current_direction
                separator()
                continue
            current_room = move_room(current_direction, current_room, rooms)
            print(f'Moved to {current_room.title()}')

            separator()
            current_command = default_command

        # Search command, gives information on whether an item is in the room or not.
        while current_command == 'search':
            if current_room not in artifacts:
                print('Nothing Found.')
                current_command = default_command
            else:
                item = None
                for i in artifacts[current_room]:
                    item = i
                    if i not in inventory:
                        print(f"You see a{'' if syllable_check(item) else 'n'} {i}")
                    else:
                        print(f"There is a spot that looks like a{'' if syllable_check(item) else 'n'} {i}.")

            separator()
            current_command = default_command

        # Pickup command. As on tin, knows if an item has been picked up already as a bonus.
        while current_command == 'pickup':
            if current_room in artifacts:
                for i in artifacts[current_room]:
                    if i in inventory:
                        print(f'Already obtained: {x_of_x_format(inventory, i)} from {current_room}')

                    else:
                        inventory.update(artifacts.get(current_room))
                        print(f'Picked up: {x_of_x_format(inventory, i)} from {current_room}')
            else:
                print('Nothing to pickup!')
            separator()
            current_command = default_command

        # Gives inventory and a cheeky message.
        while current_command == 'inventory':
            print('You have obtained:')
            if len(inventory) <= 0:
                print('Nothing.\n'
                      'A moth flies out of your bag in sadness.\n')
            else:
                for x in inventory:
                    print(f'{x_of_x_format(inventory, x)}')
            separator()

            current_command = default_command

        # Prints out a list of objectives and removes objectives already obtained.
        while current_command == 'objectives':
            print('Objectives: ')
            for i in artifacts:
                for j in artifacts[i]:
                    if j in inventory:
                        continue
                    else:
                        print(f'Retrieve the {x_of_x_format(artifacts.get(i), j)}')
            print('Defeat Villain!')
            print('\nPress any input to continue.')
            if input() == str:
                continue
            separator()
            current_command = default_command

        # Help command prints out instructions
        while current_command == 'help':
            print(f"{instructions()}\nCommands: {iterate_value(commands)}\n\nPress any input to continue.")
            if input() == str:
                continue
            separator()
            current_command = default_command

        # Added the alternate quit because I kept typing it and invalidating input.
        while current_command == 'exit' or current_command == 'quit':
            print('Are you sure you want to exit?')
            if yn_validate() == 'n':
                current_command = default_command

            separator()
            exit('Exited game.')

        # This is 'technically' not a command, the system uses commands as its current state.
        while current_command == 'bossfight':
            print(f"You have encountered the villain in the {current_room}!")
            if win_check(artifacts):
                print('You Won!')
            else:
                print('Not enough artifacts!\n\nYou Lost!')
            quit()

        # For faster testing :)
        while current_command == 'cheat':
            cheat = input().lower()

            # Gives all artifacts
            if cheat == 'allitems':
                for i in artifacts:
                    inventory.update(artifacts.get(i))
                print('All items added you filthy cheat.')

            # Removes all artifacts
            if cheat == 'putemback':
                inventory = {}

            # Removes select item from inventory list
            if cheat == 'removeitem':
                print(inventory)
                item = validate_input(inventory)
                inventory.pop(item)

            # Teleport to specific room: Must type room name exact with spaces when prompted.
            if cheat == 'tpme':
                print(rooms)
                room = validate_input(rooms)
                current_room = room
                if room == villain_room:
                    current_command = 'bossfight'

            # Straight to the good part.
            if cheat == 'bossfight':
                current_room = villain_room
                current_command = 'bossfight'
                continue
            separator()
            current_command = default_command
