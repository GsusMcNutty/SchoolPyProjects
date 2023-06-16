user_input = input()

split = user_input.split()

average = 0

in_max = 0
for i in split:
    average = average + int(i)


for i in split:
    if int(i) > in_max:
        in_max = int(i)

print('{} {}'.format(int(average / len(split)), in_max))