import csv

output = {}

with open("input1.csv", 'r') as input1:
    contents = input1.read()
    print(contents)

contents = contents.replace("\n", '')
words = contents.split(',')

for i in words:
    if i in output:
        output.update({i: output.get(i) + 1})
    else:
        output.update({i: 1})

print(output)

for i in output:
    print(f"{i} {output.get(i)}")
