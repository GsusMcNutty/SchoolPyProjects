import Movement
import Functions
import TB_Data


if __name__ == '__main__':

    inventory = {}

    commands = TB_Data.command_list()
    rooms = TB_Data.get_rooms()
    artifacts = TB_Data.get_artifacts()
    starting_command = 'help'
    default_command = 'wait'
    starting_room = 'tower room'
    # Moved villain room from design doc to better have the player traverse the level.
    villain_room = 'garden'

    current_room = starting_room
    current_command = starting_command
    running = False

    print("Initiate?")
    if Functions.yn_validate() == 'y':
        print('Initiated')
        running = True
    else:
        running = True
        current_command = 'exit'

    Functions.separator()

    while running:
        # Functions as the default command as the player waits and decides what to do next.
        while current_command == 'wait':
            print(f'Current location is: {current_room.title()}')
            if current_room == villain_room:
                current_command = 'bossfight'
            else:
                print('Awaiting a command.')
                current_command = Functions.validate_input(commands)
                Functions.separator()

        # You like to move it, move it!
        while current_command == 'move':
            directions = rooms.get(current_room).keys()
            print(f"What direction?\nYou have doors to the: {Movement.direction_commands(directions)}.")
            current_direction = Functions.validate_input(rooms.get(current_room), commands.copy(), current_command)
            if current_direction not in rooms.get(current_room):
                current_command = current_direction
                Functions.separator()
                continue
            current_room = Movement.move_room(current_direction, current_room, rooms)
            print(f'Moved to {current_room.title()}')

            Functions.separator()
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
                        print(f"You see a{'' if Functions.syllable_check(item) else 'n'} {i}")
                    else:
                        print(f"There is a spot that looks like a{'' if Functions.syllable_check(item) else 'n'} {i}.")

            Functions.separator()
            current_command = default_command

        # Pickup command. As on tin, knows if an item has been picked up already as a bonus.
        while current_command == 'pickup':
            if current_room in artifacts:
                for i in artifacts[current_room]:
                    if i in inventory:
                        print(f'Already obtained: {Functions.x_of_x_format(inventory, i)} from {current_room}')

                    else:
                        inventory.update(artifacts.get(current_room))
                        print(f'Picked up: {Functions.x_of_x_format(inventory, i)} from {current_room}')
            else:
                print('Nothing to pickup!')
            Functions.separator()
            current_command = default_command

        # Gives inventory and a cheeky message.
        while current_command == 'inventory':
            print('You have obtained:')
            if len(inventory) <= 0:
                print('Nothing.\n'
                      'A moth flies out of your bag in sadness.\n')
            else:
                for x in inventory:
                    print(f'{Functions.x_of_x_format(inventory, x)}')
            Functions.separator()

            current_command = default_command

        # Prints out a list of objectives and removes objectives already obtained.
        while current_command == 'objectives':
            print('Objectives: ')
            for i in TB_Data.artifacts:
                for j in TB_Data.artifacts[i]:
                    if j in inventory:
                        continue
                    else:
                        print(f'Retrieve the {Functions.x_of_x_format(TB_Data.artifacts.get(i), j)}')
            print('Defeat Villain!')
            print('\nPress any input to continue.')
            if input() == str:
                continue
            Functions.separator()
            current_command = default_command

        # Help command prints out instructions
        while current_command == 'help':
            print(f"{TB_Data.instructions()}\nCommands: {Functions.iterate_value(commands)}\n\nPress any input to continue.")
            if input() == str:
                continue
            Functions.separator()
            current_command = default_command

        # Added the alternate quit because I kept typing it and invalidating input.
        while current_command == 'exit' or current_command == 'quit':
            print('Are you sure you want to exit?')
            if Functions.yn_validate() == 'n':
                current_command = default_command

            Functions.separator()
            exit('Exited game.')

        # This is 'technically' not a command, the system uses commands as its current state.
        while current_command == 'bossfight':
            print(f"You have encountered the villain in the {current_room}!")
            if Functions.win_check(artifacts, inventory):
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
                item = Functions.validate_input(inventory)
                inventory.pop(item)

            # Teleport to specific room: Must type room name exact with spaces when prompted.
            if cheat == 'tpme':
                print(rooms)
                room = Functions.validate_input(rooms)
                current_room = room
                if room == villain_room:
                    current_command = 'bossfight'

            # Straight to the good part.
            if cheat == 'bossfight':
                current_room = villain_room
                current_command = 'bossfight'
                continue
            Functions.separator()
