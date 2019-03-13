str = 'Привет Мир Ласковый Лига Личный'
str = str.split(' ')
for i in range(0, len(str)):
    if str[i][0] == 'Л' and str[i][1] == 'и':
        print(str[i])