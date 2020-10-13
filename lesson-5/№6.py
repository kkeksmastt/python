import re
with open('lessons.txt', encoding='utf-8') as f_obj:
    my_dict = {}
    for i in f_obj.readlines():
        my_str = re.sub(r'\([^()]*\)', '', i).split()
        my_str[0] = my_str[0].strip(':')
        for el in my_str:
            if '—' in my_str:
                my_str.remove('—')
        name = my_str.pop(0)
        my_str = [int(b) for b in my_str]
        less = sum(my_str)
        my_dict[name] = less
print(my_dict)

