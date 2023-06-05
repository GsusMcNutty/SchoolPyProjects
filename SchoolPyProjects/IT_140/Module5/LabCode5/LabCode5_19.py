# Define your function here
def plural_check(val):
    if val > 1:
        return 's'
    return ''


def dollar_split(change):
    output = []
    if len(change) >= 3:
        output.append(change[0:len(change) - 2])
    else:
        output.append(0)
    if len(change) >= 1:
        output.append(change[len(change) - 2:len(change)])
    return output


def exact_change(tendered):
    dictionary = {}
    split_tendered = [dollar_split(str(tendered))[0], dollar_split(str(tendered))[1]]
    dollars = int(split_tendered[0])
    cents = int(split_tendered[1])
    quarters = 0
    nickels = 0
    dimes = 0
    pennies = 0
    dictionary.clear()
    dictionary.update({'dollar': dollars})

    if cents >= 25:
        quarters = int(cents / 25)
        cents = cents % 25
    if cents >= 10:
        dimes = int(cents / 10)
        cents = cents % 10
    if cents >= 5:
        nickels = int(cents / 5)
        cents = cents % 5
    if cents >= 1:
        pennies = int(cents / 1)
        cents = cents % 1

    dictionary.update({'quarter': quarters})
    dictionary.update({'dime': dimes})
    dictionary.update({'nickel': nickels})
    dictionary.update({'penny': pennies})

    return dollars, quarters, dimes, nickels, pennies


def print_money(dollar, quarter, dime, nickel, penny):
    if dollar > 0:
        print('{} {}{}'.format(dollar, 'dollar', plural_check(dollar)))
    if quarter > 0:
        print('{} {}{}'.format(quarter, 'quarter', plural_check(quarter)))
    if dime > 0:
        print('{} {}{}'.format(dime, 'dime', plural_check(dime)))
    if nickel > 0:
        print('{} {}{}'.format(nickel, 'nickel', plural_check(nickel)))
    if penny > 0:
        print('{} {}{}'.format(penny, 'penn', 'ies' if plural_check(penny) == 's' else 'y'))


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val > 0:
        print_money(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)
    else:
        print('no change')
    # Type your code here.
