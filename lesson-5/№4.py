
with open('numbers') as f_obj:
    with open('numbers on rus', 'w+', encoding='utf-8')as f_obj2:
        i = 0
        while i < 4:
            text = f_obj.readline()
            if 'One' in text:
                f_obj2.write('Один - 1\n')
            elif 'Two' in text:
                f_obj2.write('Два - 2\n')
            elif 'Three' in text:
                f_obj2.write('Три - 3\n')
            elif 'Four' in text:
                f_obj2.write('Четыре - 4\n')
            i += 1

