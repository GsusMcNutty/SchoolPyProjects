print('Give a character to see how many times it occurs')
print('n voluntary sentence')
string_in = input('\n')

string_list = string_in.split(' ', 1)

letter = string_list[0]
word = string_list[1]


def math_count(letter, word):
    return int(len(word.split(letter)) - 1)


def letter_count(letter, word):
    return word.count(letter)


print('\nUsing Math, the letter/digit occurs:', str(math_count(letter, word)), 'times')

print('Using functions, the letter/digit occurs:', letter_count(letter, word), 'times')