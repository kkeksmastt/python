def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        print(f)
    yield f


for i in fact(3):
    print('Факториал вашего числа равен:', i)
