cont = 'Yes'
fio = ['Ельцин', 'Путин', 'Ленин', 'Горбачев', 'Сталин']  # можно словарем сделать, но ломает ))
yob = [1931, 1952, 1870, 1931, 1878]
ans = []
while cont == 'Yes':
    for i in range(len(fio)):
        ans_str = 'В каком году родился ' + str(fio[i]) + ': '
        answer = int(input(ans_str))
        if answer == yob[i]:
            ans.append(1)
        else:
            ans.append(0)
    print("Правильных ответов: ", sum(ans))
    print("Ошибок: ", len(ans) - sum(ans))
    print("Процент правильных ответов: ", sum(ans) * 100 / len(ans), "%")
    print("Процент неправильных ответов: ", 100 - sum(ans) * 100 / len(ans), "%")
    cont = input('Продолжить игру? (Yes/No)  ')
print('Good Luck')
