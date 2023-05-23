name = input('FirstName MiddleName LastName\n')
name_arr = name.split(' ')

if len(name_arr) == 3:
    first_name = name_arr[0].upper()
    middle_name = name_arr[1].upper()
    last_name = name_arr[2]
    print('{}{}, {}.{}.'.format(last_name[0].upper(), last_name[1:], first_name[0].upper(), middle_name[0].upper()))
if len(name_arr) == 2:
    first_name = name_arr[0].upper()
    last_name = name_arr[1]
    print('{}{}, {}.'.format(last_name[0].upper(), last_name[1:], first_name[0].upper()))
if len(name_arr) == 1:
    first_name = name_arr[0]