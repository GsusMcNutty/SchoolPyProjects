user_input = input()
hourly_temperature = user_input.split()

split = user_input.split()
split.sort()

for count, i in enumerate(split):
    print(count)
    if count < len(split) - 1:
        print('{} -> '.format(i), end='')
    else:
        print('{}'.format(i))

