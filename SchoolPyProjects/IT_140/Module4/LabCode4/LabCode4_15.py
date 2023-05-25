word = input("Give me a password with 'i', 'a', 'm', 'B', or 'o'; I'll make it stronger! TM\n")
password_out = ''


def pass_change(password):
    password = password.replace('i', '!')
    password = password.replace('a', '@')
    password = password.replace('m', 'M')
    password = password.replace('B', '8')
    password = password.replace('o', ".")
    password = password + 'q*s'
    return password


print("Your new password is: {}".format(pass_change(word)))


def pass_change_hard(password):
    for i, v in enumerate(password):
        if v == 'i':
            password = password[:i] + '!' + password[i + 1:]
        if v == 'a':
            password = password[:i] + '@' + password[i + 1:]
        if v == 'm':
            password = password[:i] + 'M' + password[i + 1:]
        if v == 'B':
            password = password[:i] + '8' + password[i + 1:]
        if v == 'o':
            password = password[:i] + '.' + password[i + 1:]
    password = password + 'q*s'
    return password


print("Hard Mode password is: {}".format(pass_change_hard(word)))
