def int_check(check):
    if check.isdigit():
        return 1
    return -1


def yn_check(check):
    if check.lower() == 'y' or check.lower() == 'n':
        return 1
    return -1


hours_worked = input('How many hours did you work?\n')
'''
if int_check(hours_worked) == -1:
    print('Error: Not a float or integer.')
    hours_worked = input('How many hours did you work?\n')
    hours_worked.isdecimal()
'''

base_pay = input('What is your base pay?\n')
'''
if int_check(base_pay) == -1:
    print('Error: Not a float or integer.')
    base_pay = input('What is your base pay?\n')
'''
standard_ot = input('Is your overtime time and a half? (Y/N)\n')
if yn_check(standard_ot) == -1:
    print('Error: Please give a Y or N.')
    standard_ot = input('Is your overtime time and a half? (Y/N)\n')

if standard_ot.lower() == 'n':
    ot_pay = input('How much is your over time pay?\n')
    '''
    if int_check(ot_pay) == -1:
        print('Error: Not a float or integer.')
        ot_pay = input('How much is your over time pay?\n')
    '''
else:
    ot_pay = float(base_pay) + (float(base_pay) * 0.5)

standard_threshold = input('Is your overtime threshold 40 hours? (Y/N)\n')
if yn_check(standard_threshold) == -1:
    print('Error: Please give a Y or N.')
    standard_threshold = input('Is your overtime threshold 40 hours? (Y/N)\n')

if standard_threshold.lower() == 'n':
    ot_threshold = input('What is your over time threshold?\n')
    if int_check(ot_threshold) == -1:
        print('Error: Not a float or integer.')
        ot_threshold = input('What is your over time threshold?\n')
else:
    ot_threshold = 40


# def for splitting the hours into ot and base
def hours_split(hours_in, threshold):
    hours_list = [0, 0]
    hours_difference = hours_in - threshold
    if hours_difference <= 0:
        hours_list[0] = hours_difference + threshold
        hours_list[1] = 0
    if hours_difference > 0:
        hours_list[0] = threshold
        hours_list[1] = hours_difference
    return hours_list  # output array


# pay calculator
def pay_calculate(hours_in, pay):
    return hours_in * pay


# main function to add pay
def main_function(base, ot):
    return base + ot


hours = hours_split(float(hours_worked), float(ot_threshold))
total_base = pay_calculate(hours[0], float(base_pay))
total_ot = pay_calculate(hours[1], float(ot_pay))

print('Base Hours: {:.2f} Rate: ${:.2f} Paid: ${:.2f}'.format(hours[0], float(base_pay), total_base))
print('Overtime: {:.2f} Rate: ${:.2f} Paid: ${:.2f}'.format(hours[1], float(ot_pay), total_ot))
print('\nTotal: ${:.2f}'.format(main_function(total_base, total_ot)))
