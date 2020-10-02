product_num = 1
products = []
analytics = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}
while True:
    user_answer = input('Хотите добавить товары? Да или нет. ')
    user_answer = user_answer.lower()
    if user_answer == 'да':
        user_product = input('Введите название товара ')
        cost = input('Введите стоимость товара ')
        amount = input('Сколько товара имеется ')
        unit = input('В чем измеряется ')
        products.append((product_num, {'название': user_product, 'цена': cost, 'количество': amount, 'ед': unit}))
        product_num += 1
        analytics['название'].append(user_product)
        analytics['цена'].append(cost)
        analytics['количество'].append(amount)
        analytics['ед'].append(unit)
    elif user_answer == 'нет':
        break
    else:
        print('Не верный ввод, попробуйте снова')
for i in products:
    print(i)
user_answer = input('Вывести аналитику? Да или нет')
user_answer = user_answer.lower()
if user_answer == 'да':
    print(analytics)
