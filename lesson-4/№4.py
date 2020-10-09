my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list2 = my_list.copy()
my_list2.sort()
new_list = [x for x in my_list2 if x != my_list2[my_list2.index(x)+1]]
new_list2 = [x for x in my_list if x in new_list]
print(new_list2)
