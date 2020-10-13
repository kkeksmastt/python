with open('for №3.txt') as f_obj:
    workers = 0
    sum_of_salary = 0
    low_salary = []
    txt = f_obj.readlines()
    b = len(txt)
    i = 0
    while b > i:
        salary = int(txt[i].split()[1])
        if salary > 20000:
            sum_of_salary += int(txt[i].split()[1])
            workers += 1
        else:
            low_salary.append(txt[i].split()[0])
        i += 1
    average_salary = sum_of_salary / workers
    print(f'Те, чья зарплата меньше 20000: {low_salary}. Средняя зарплата: {average_salary}.')
