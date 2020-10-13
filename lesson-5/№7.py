import json
with open('firm.txt', encoding='utf-8') as f_obj:
    my_list = []
    my_dict = {}
    average_profit = 0
    num_of_firm = 0
    for i in f_obj.readlines():
        i = i.split()
        i[len(i)-1] = i[len(i)-1].strip('.')
        firm_name = i.pop(0)
        i.pop(0)
        i = [int(x) for x in i]
        profit = i[0] - i[1]
        my_dict[firm_name] = profit
        if profit > 0:
            num_of_firm += 1
            average_profit = (average_profit + profit) / num_of_firm
    my_list.append(my_dict)
    my_list.append(dict(average_profit=average_profit))

with open('json.json', 'w') as f_obj2:
    json.dump(my_list, f_obj2)
print(my_list)
