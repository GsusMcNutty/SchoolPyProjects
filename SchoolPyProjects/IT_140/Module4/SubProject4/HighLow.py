user_input = int(input('Input a value between 1-10\n'))
number = 4

while user_input != number:
    if user_input > number:
        print('Lower.')
    if user_input < number:
        print('Higher.')
    user_input = int(input('Guess again.\n'))

print('It was {}! You guessed it correctly!'.format(number))
