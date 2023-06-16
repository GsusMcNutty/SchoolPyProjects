def validate_input(command_dict, optional=None, remove_commands=None):
    command = input().lower()
    if optional is not None:
        optional.remove(remove_commands)
    if optional is None:
        optional = []
    # print(optional)
    while command not in command_dict:
        if command in optional:
            break
        command = input("Invalid input, try another\n").lower()
    # print(direction)
    return command


def yn_validate():
    string = input('Y/N?\n').lower()
    while string != 'y' and string != 'n' and string != 'yes' and string != 'no':
        print('Invalid input: Y/N')
        string = input().lower()
    return string[0]
