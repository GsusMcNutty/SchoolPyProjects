def validate_input(command_dict, optional=None, remove_commands=None):
    command = input().lower()
    if optional is not None:
        optional.remove(remove_commands)
    if optional is None:
        optional = []
    print(optional)
    while command not in command_dict:
        if command in optional:
            break
        command = input("Invalid input, try another\n")
    # print(direction)
    return command


def yn_validate():
    string = input('Y/N?\n').lower()
    while string != 'y' and string != 'n':
        print('Invalid input: Y/N')
        string = input().lower()
    return string


def move_room(direction, current_location, rooms_dict):
    return rooms_dict.get(current_location).get(direction)


def direction_commands(cardinals):
    cardinals = str(cardinals)
    cardinals = cardinals[cardinals.index('[') + 1: cardinals.index(']')]
    return cardinals.replace("'", '').title()

if __name__ == '__main__':


    command_list = ['move', 'wait', 'exit']
    default_command = 'wait'
    starting_room = 'tower room'

    current_room = starting_room
    current_command = default_command
    running = False

    print("Initiate?")
    if yn_validate() == 'y':
        print('initiated')
        running = True
    else:
        running = True
        current_command = 'exit'

    while running:
        while current_command.lower() == 'wait':
            print('Awaiting a command.')
            current_command = validate_input(command_list)

        while current_command.lower() == 'move':
            print('Current location is: {}. Where to?'.format(current_room))
            current_direction = validate_input(rooms.get(current_room),
                                               command_list.copy(), current_command)
            print(current_direction)
            if current_direction not in rooms.get(current_room):
                current_command = current_direction
                break
            print(command_list)
            current_room = move_room(current_direction, current_room, rooms)
            print('Moved to {}'.format(current_room))
            current_command = default_command

        while current_command.lower() == 'exit':
            print('Are you sure you want to exit?')
            if yn_validate() == 'n':
                current_command = default_command
                break
            exit('Exited game')
