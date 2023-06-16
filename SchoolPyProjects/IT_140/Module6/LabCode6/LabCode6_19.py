user_replacements = input()
sentence = input()

split = user_replacements.split()
test_replace = 'automobile'
new_sentence = ''

word_dict = {}

for count, i in enumerate(split):
    if count % 2 == 0:
        word_dict[i] = split[count + 1]

for i in word_dict:
    sentence = sentence.replace(i, word_dict.get(i))

print(sentence)
