num_month = int(input('Введите месяц числом '))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if winter.count(num_month):
    print('Зима')
elif spring.count(num_month):
    print('Весна')
elif summer.count(num_month):
    print('Лето')
elif autumn.count(num_month):
    print('Осень')
else:
    print('Такого месяца нет')
