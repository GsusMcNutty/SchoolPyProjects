year = int(input())

if year <= 1900:
    print('Long ago')
elif 1901 <= year <= 2000:
    print('20th century')
elif 2001 <= year < 2101:
    print('21st century')
else:
    print('Distant future')
