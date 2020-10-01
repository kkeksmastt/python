max_number = 0
number = int(input('Введите целое, положительное число '))
while 1>0:
    last_number = number % 10
    number = int(number / 10)
    if last_number > max_number:
        max_number = last_number
    if number == 0:
        break
print(max_number)
