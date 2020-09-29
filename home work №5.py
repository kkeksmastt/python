revenue = int(input('Введите выручку '))
cost = int(input('Введите издержки '))
profit = revenue - cost
if revenue > cost:
    print('Вы получаете прибыль')

    profitability = profit / revenue
    print(f'Рентабильность  {profitability} к 1')
    # не понял часть задания с рентабильностью,
    # его стоило как-то перефразировать

    number_of_staff = int(input('Сколько у вас сотрудников? '))
    profit_on_one_staff = profit / number_of_staff
    profit_on_one_staff = int(profit_on_one_staff)
    print(f'Прибыль в расчете на одного сотрудника: {profit_on_one_staff}!')
elif revenue < cost:
    print('Вы в убытке')
else:
    print('Вы выходите в 0')
