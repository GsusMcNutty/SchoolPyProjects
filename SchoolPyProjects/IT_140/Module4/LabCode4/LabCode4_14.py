user_text = input("Give me a string and I'll count the letters.\n")


def character_id(string):
    string = string.casefold()
    non_alphabet_count = 0
    for i in string:
        if 96 <= ord(i) <= 123 or ord(i) == 33:
            non_alphabet_count += 1
            # print(i, ord(i))
    return non_alphabet_count


print(character_id(user_text))
