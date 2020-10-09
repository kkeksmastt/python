def my_func(num1=0, num2=1, num3=2):
    return max(num1, num2) + max(num2, num3)


z, x, c = 10, 20, 30
print(my_func(z, x, c))
