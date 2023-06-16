user_input = input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for count, i in enumerate(mult_table):
    for c2, j in enumerate(i):
        if c2 < len(i) - 1 :
            print(j, end=' | ')
        else:
            print(j, end='')
        count += 1
    print()

