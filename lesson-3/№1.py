def division(num1, num2):
    try:
        b = num1 / num2
        return b
    except ZeroDivisionError:
        return 'Zero division'


x, a = int(input('give num ')), int(input('give num two '))
print(division(x, a))
