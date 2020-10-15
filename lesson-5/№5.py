with open('num', 'w') as f_obj:
    f_obj.write('1 2 3 4 5 6 7 8 9')
with open('num') as f_obj2:
    numbers = f_obj2.read().split()
    numbers = [int(i) for i in numbers]
    print(sum(numbers))