import Validators
import Movement
import Text_Based_Adventure_Data


def direction_list(cardinals):
    cardinals = str(cardinals)
    cardinals = cardinals[cardinals.index('[') + 1: cardinals.index(']')]
    return cardinals.replace("'", '').title()


if __name__ == '__main__':

    commands = Text_Based_Adventure_Data.command_list()
    rooms = Text_Based_Adventure_Data.room_dictionary()
    print(commands)
    default_command = 'wait'
    starting_room = 'tower room'

    current_room = starting_room
    current_command = default_command
    running = False

    print("Initiate?")
    if Validators.yn_validate() == 'y':
        print('Initiated')
        running = True
    else:
        running = True
        current_command = 'exit'

    while running:
        while current_command == 'wait':
            print('Current location is: {}'.format(current_room.title()))
            print('Awaiting a command.')
            current_command = Validators.validate_input(commands)

        while current_command == 'move':
            directions = rooms.get(current_room).keys()
            print('What direction?')
            # Debug below
            print('You have doors to the: {}'.format(direction_list(directions)))
            current_direction = Validators.validate_input(rooms.get(current_room),
                                                          commands.copy(), current_command)
            # print(current_direction)
            if current_direction not in rooms.get(current_room):
                current_command = current_direction
                break
            current_room = Movement.move_room(current_direction, current_room, rooms)
            print('Moved to {}'.format(current_room.title()))
            current_command = default_command

        while current_command == 'exit' or current_command == 'quit':
            print('Are you sure you want to exit?')
            if Validators.yn_validate() == 'n':
                current_command = default_command
                break
            exit('Exited game')
