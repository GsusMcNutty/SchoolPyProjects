user_input = input()

split = user_input.split()
word_dict = {}
for i in split:
    if word_dict.get(i) is None:
        word_dict[i] = 1
    else:
        word_dict.update({i: word_dict.get(i) + 1})

for i in split:
    print(i, word_dict.get(i))
