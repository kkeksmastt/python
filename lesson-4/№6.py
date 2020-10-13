from itertools import count, cycle, islice


user_answer = int(input('С какого числа начать? '))
for i in islice(count(user_answer), 5):
    print(i)


traffic_lights = ['red', 'yellow', 'green', 'yellow']
for i in islice(cycle(traffic_lights), 10):
    print(i)
