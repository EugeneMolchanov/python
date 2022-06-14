# 1 задание

#name = input('Имя: ')
#last_name = input('Фамилия: ')
#age = input('Возраст: ')
#print (name, last_name, ',' , age , 'добро пожаловать!')

# 2 задание

# sec = int(input('Введите число:'))
# hour = int(sec // 3600)
# minutes = sec % 3600 // 60
# seconds = sec % 60
# print ('Часов', hour)
# print ('minut', minutes)
# print ('secs', seconds)

# 3 задание

# num = int(input ('Введите число: '))
# num_1 = num
# num_2 = num * 11
# num_3 = num * 111
# res = num_1 + num_2 + num_3
# print (res)

# 4 задание

# num = int(input('Введите число: '))
# big = num % 10
# print (big)
# while num > 1:
#     num = num // 10
#     print (num)
#     if num % 10 > big:
#         print (num)
#         print (big)
#         big = num % 10
#         print (big)
#     elif num > 9:
#         pass
# print('Самая большая цифра: ', big)

# 5 задание

# vyruchka = int(input('Введите сумму выручки: '))
# izderzhki = int(input('Введите сумму издержек: '))
# if izderzhki > vyruchka:
#     print('Сработали в убыток')
# elif vyruchka > izderzhki:
#     pribyl = vyruchka - izderzhki
#     print('Прибыль составила: ', pribyl)
#     rent = pribyl / vyruchka
#     print('Рентабельность: {:.2f}'.format(rent))
#     count = int(input('Введите количество сотрудников: '))
#     print(f'Прибыль в расчете на одного сотрудника составила: {int(pribyl / count)}')
# else:
#     print('Сработали в убыток.')