user_input = input()
string_list = [user_input.split(' ')[0], user_input.split(' ')[1]]


def run_program(word, number):
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))


while string_list[0] != 'quit':
    run_program(string_list[0], string_list[1])
    user_input = input()
    string_list = [user_input.split(' ')[0], user_input.split(' ')[1]]
