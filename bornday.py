Pushkin_year_born = 1799
Pushkin_day_born="26 мая"
answer=input('Напишите год рождения АС Пушкина: ')
if int(answer)==Pushkin_year_born:
    answer=input('Напишите день рождения АС Пушкина: ')
    if answer==Pushkin_day_born:
        print('Верно')
    else:
        print('Не верно')
else:
    print('Не верный год рождения')