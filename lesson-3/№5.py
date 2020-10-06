def my_func(numbers):
    while True:
        b = 0
        for i in numbers:
            try:
                numbers[b] = int(i)
            except ValueError:
                pass
            b += 1
        if numbers[len(numbers)-1] == 'q':
            numbers.pop()
            summ = sum(numbers)
            if summ != 0:
                print(summ)
            print('exit')
            break
        else:
            summ = sum(numbers)
            print(summ)
            new_numbers = input('give more numbers, press q for quit ').lower().split()
            for i in new_numbers:
                numbers.append(i)


a = input('give numbers, press q for quit ').lower().split()
my_func(a)
