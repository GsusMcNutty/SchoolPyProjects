output = {}

with open('file1.txt', 'r') as input1:
    contents = input1.readlines()
    # print(contents)

number = ''
word = ''

for count, i in enumerate(contents):
    if count % 2 != 0:
        contents[count] = i[0:len(i) - 1]
    else:
        contents[count] = i[0:len(i) - 1]

# print(contents)

for count, i in enumerate(contents):
    if count % 2 == 0:
        if i in output:
            output[i] = output.get(i) + '; ' + contents[count + 1]
        else:
            output[i] = contents[count + 1]

sorted_output = {}
sort_output = sorted(output)
for i in sort_output:
    sorted_output[i] = output.get(i)

with open('output_keys.txt', 'w') as key_file:
    for i in sorted_output:
        key_file.write(f"{int(i)}: {sorted_output.get(i)}\n")

titles = []
for i in sorted_output:
    split = sorted_output.get(i).split('; ')
    for j in split:
        titles.append(j)

titles = sorted(titles)

with open('output_titles.txt', 'w') as key_file:
    for i in titles:
        key_file.write(f"{i}\n")
