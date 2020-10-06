my_list = []
while True:
    user_answer = input('Хотите добавить элементы? да или нет ')
    user_answer = user_answer.lower()
    if user_answer == 'да':
        user_element = input('Что добавить? ')
        try:
            user_element = int(user_element)
        except ValueError:
            pass
        my_list.append(user_element)
    elif user_answer == 'нет':
        break
    else:
        print('Не известный ответ')
i = 0
while i < len(my_list):
    a = my_list.pop(i)
    my_list.insert(i+1, a)
    i += 2
print(my_list)
