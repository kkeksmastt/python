how_run = int(input('Сколько спортсмен пробежал в первый день? '))
how_need = int(input('Сколько всего за бень он должен пробежать? '))
day_number = 1
while how_run <= how_need:
    how_run = how_run / 100 * 110
    day_number += 1
    print(f'{day_number}-й день: {how_run}')
print(f'На {day_number}-й день спортсмен достиг результата - не менее {how_need} км.')

