num_rows = int(input())
num_cols = int(input())

a_save = 65
rowed = 0
coled = 0
r = 1

while rowed < num_rows:
    coled = 0
    rowed += 1
    a = a_save

    while coled < num_cols:
        coled += 1
        print('{}{}'.format(r, chr(a)), end=' ')
        a += 1
    r += 1
print()

