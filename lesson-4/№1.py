from sys import argv
argv = argv[1:]
if 'h' in argv:
    print('Данный скрипт выполняет расчет заработной платы. Формула расчета: (выработка в часах * ставка в час) + премия ')
else:
    print('Ваша зарплата:', (int(argv[0]) * int(argv[1])) + int(argv[2]))
