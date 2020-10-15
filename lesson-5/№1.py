with open('123', 'w') as f_obj:
    while True:
        txt = input('Введите текст, чтобы закончитить, введите пустую строку ')
        if txt == '':
            break
        else:
            f_obj.write(txt+'\n')
