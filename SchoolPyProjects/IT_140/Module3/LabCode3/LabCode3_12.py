# Seasons

input_month = input('Month?\n')
input_day = input('Day?\n')

month_dict = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}

season_dict = {
    'january': 'winter',
    'february': 'winter',
    'march': 'winter_spring',
    'april': 'spring',
    'may': 'spring',
    'june': 'spring_summer',
    'july': 'summer',
    'august': 'summer',
    'september': 'summer_autumn',
    'october': 'autumn',
    'november': 'autumn',
    'december': 'autumn_winter',
}
transition_dict = {
    'winter_spring': 20,
    'spring_summer': 21,
    'summer_fall': 22,
    'autumn_winter': 21
}


def month_validate(month, day):
    for i in month_dict.keys():
        if i == month.lower():
            if 0 < int(day) <= int(month_dict.get(i)):
                return 1
            else:
                return -1
    return -1


def season_check(month, day):
    season = season_dict[month.lower()]
    for i in transition_dict:
        if i == season:
            if int(day) < int(transition_dict[season_dict[month.lower()]]):
                return '{}'.format(season[0: season.find('_')])
            if int(day) >= int(transition_dict[season_dict[month.lower()]]):
                return '{}'.format(season[season.find('_') + 1:])
    return '{}'.format(season)


def main_function(month, day):
    if month_validate(month, day) != 1:
        return 'Invalid'
    else:
        output_season = season_check(input_month, input_day)
        return '{}{}'.format(output_season[0].upper(), output_season[1:])


print(main_function(input_month, input_day))
