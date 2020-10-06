year = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
num_month = int(input('Введите номер месяца '))
if num_month in year.get('winter'):
    print('Это Зима')
elif num_month in year.get('spring'):
    print('Это Весна')
elif num_month in year.get('summer'):
    print('Это Лето')
elif num_month in year.get('autumn'):
    print('Это Осень')
else:
    print('Такого месяца нет')
