

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


def direction_list(cardinals):
    cardinals = str(cardinals)
    cardinals = cardinals[cardinals.index('[') + 1: cardinals.index(']')]
    return cardinals.replace("'", '').title()


def separator():
    print(''.rjust(100, '_'))


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


def win_check(collection, held):
    win = True
    for a in collection:
        for b in collection[a]:
            if b in held:
                print(f"Attacked with: {str(b).title()} of {str(held.get(b)).title()}")
            else:
                win = False
                break
    return win


def syllable_check(word):
    vowels = 'aeiou'
    syllable = True

    if vowels.find(word[0]) != -1:
        syllable = False

    return syllable


