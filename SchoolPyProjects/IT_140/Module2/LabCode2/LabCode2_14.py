# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = input('Enter favorite number :\n')

print('You entered: {} {} {}'.format(favorite_color, favorite_flower, favorite_number + '\n'))


password1 = '{}_{}'.format(favorite_color, favorite_flower)
print('First password: ' + password1)
password2 = '{}{}{}'.format(favorite_number, favorite_color, favorite_number)
print('Second password: ' + password2 + '\n')

print('Number of characters in {}: {}'.format(password1, len(password1)))
print('Number of characters in {}: {}'.format(password2, len(password2)))
