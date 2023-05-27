user_input = int(input('Input a value between 1-10\n'))
condition = 4

while user_input != condition:
    if user_input > condition:
        print('Lower.')
    if user_input < condition:
        print('Higher.')
    user_input = int(input('Guess again.\n'))

print('It was {}! You guessed it correctly!'.format(condition))
