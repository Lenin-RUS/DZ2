Pushkin_year_born = 1799
Pushkin_day_born="26 мая"

answer=input('Напишите год рождения АС Пушкина: ')

while int(answer)!=Pushkin_year_born:
    answer=input('Напишите год рождения АС Пушкина: ')


while True:
    answer=input('Напишите день рождения АС Пушкина: ')
    if answer==Pushkin_day_born:
        print('Верно')
        break
