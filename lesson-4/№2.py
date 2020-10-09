my_list = [123, 35, 2, 1, 12, 17, 15, 13, 18]
new_list = [x for x in my_list if x > my_list[my_list.index(x) - 1]]
print(new_list)
