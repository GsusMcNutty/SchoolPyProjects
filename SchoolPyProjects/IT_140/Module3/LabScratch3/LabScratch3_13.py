tendered_input = input('Input a number to receive it in change.\n')
change_dict = {
}


def tender_validate(tendered):
    if not tendered.isdigit():
        return -1
    if int(tendered) <= 0:
        return 0
    return 1


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


def change_build(tendered, dictionary):
    split_tendered = [dollar_split(tendered)[0], dollar_split(tendered)[1]]
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


def run_function(tendered, dictionary):
    if tender_validate(tendered) == -1:
        print('Invalid')
        return
    if tender_validate(tendered) == 0:
        print('No change')
        return

    change_build(tendered, dictionary)
    dollar = dictionary.get('dollar')
    quarter = dictionary.get('quarter')
    dime = dictionary.get('dime')
    nickel = dictionary.get('nickel')
    penny = dictionary.get('penny')

    if dollar > 0:
        print('{} {}{}'.format(dollar, 'Dollar', plural_check(dollar)))
    if quarter > 0:
        print('{} {}{}'.format(quarter, 'Quarter', plural_check(quarter)))
    if dime > 0:
        print('{} {}{}'.format(dime, 'Dime', plural_check(dime)))
    if nickel > 0:
        print('{} {}{}'.format(nickel, 'Nickel', plural_check(nickel)))
    if penny > 0:
        print('{} {}{}'.format(penny, 'Penn', 'ies' if plural_check(penny) == 's' else 'y'))


# print(tender_validate(tendered_input))
# print(dollar_split(tendered_input))
run_function(tendered_input, change_dict)