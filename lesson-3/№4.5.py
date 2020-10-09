def my_func(x, y):
    i = 1
    b = x
    while i < -y:
        b = b * x
        i += 1
    b = 1 / b
    return b


print(my_func(2, -3))
