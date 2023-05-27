triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')


def triangle_build(height, symbol):
    build = ''
    x = 0
    while x < height:
        build = str('{} '.format(build + symbol))
        x += 1
        print(build)


triangle_build(triangle_height, triangle_char)
