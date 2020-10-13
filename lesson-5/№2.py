with open('for №2.txt') as f_obj:
    a = f_obj.readlines()
    num_of_str = len(a)
    print(f'Общее кол-во строк: {num_of_str}')
    for b, i in enumerate(a, 1):
        print(f'Строка №{b}, количество слов: {len(i.split())}')
