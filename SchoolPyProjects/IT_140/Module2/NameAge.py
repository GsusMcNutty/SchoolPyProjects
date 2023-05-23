user_name = input('What is your name?\n')

current_year = 2023

user_age = input('How old are you?\n')


def int_check(check):
    if check.isdigit():
        return 1
    return -1


def running_check(check):
    while int_check(check) < 0:
        print('Invalid input: Not an Integer, try again please.')
        check = input('How old are you?\n')
        int_check(check)
    return check


def age_check(check):
    check_number = 0
    while int(check) > 99 and check_number == 0:
        print('Invalid input: I doubt you are that age.')
        check = input('How old are you really?\n')
        check = running_check(check)
        check_number += 1

    while int(check) > 99 and check_number == 1:
        print("Invalid input: You're serious?.")
        check = input('How old are you really?\n')
        check = running_check(check)
        check_number += 1

    while int(check) > 99 and check_number == 2:
        print("Invalid input: Ok, Dorian Gray. Last chance")
        check = input('How old are you really?\n')
        check = running_check(check)
        check_number += 1

    if int(check) < 99 and check_number != 0:
        print('That is more believable, but')

    if int(check) > 99 and check_number != 0:
        print("Well I'll be...")

    if int(check) >= 2023:
        print('BCE?!?!??')

    if int(check) == 246:
        print('Birth of the USA, eh?')

    if 121 >= int(check) >= 245:
        print('Which president have you met?')

    if 120 >= int(check) >= 113:
        print('Better call Guinness')

    if 112 >= int(check) >= 99:
        print('Almost a world record.')

    if 18 >= int(check) >= 16:
        print("You're still in high school?")

    if 15 >= int(check) >= 4:
        print("You're some kind of prodigy eh?")

    if int(check) < 3:
        print("Goo Goo, Ga ga.")

    return check


user_age = running_check(user_age)
user_age = age_check(user_age)

user_birthday_passed = input('Has your birthday passed? Y/N \n')


def passed_checker(check):
    if check.lower() == 'y' or check.lower() == 'n':
        return 1
    return -1


while passed_checker(user_birthday_passed) < 0:
    print('Invalid input, try again please.')
    user_birthday_passed = input('Has your birthday passed? Y/N \n')
    passed_checker(user_birthday_passed)


def current_age(year, age):
    return year - age


def name_age(name, age, passed):
    if passed.lower() == 'y':
        print('Hello', name + '! You were born in', str(age) + '.\n')
    elif passed.lower() == 'n':
        print('Hello', name + '! You were born in', str((age - 1)) + '.\n')


name_age(user_name, current_age(current_year, int(user_age)), user_birthday_passed)
