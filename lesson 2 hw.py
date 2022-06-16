# 1 задание

# li = [1, 2.5, 'dammit', False, [3,4]]
# print(type(li[0]))
# print(type(li[1]))
# print(type(li[2]))
# print(type(li[3]))
# print(type(li[4]))

# 2 задание

# li = [1, 2, 3, 4]
# li[0], li[1]  = li[1], li[0]
# li[2], li[3] = li[3], li[2]
# print(li)

# 3 задание
#*** Решение через keys: ***#

# months = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
# num = int(input('Введите цифру месяца: '))
# for res in months:
#     if num in months [res]:
#         print(res)
#         break
# else:
#     print ('Ошибка, такого месяца не существует')
# print('Конец')
#
# #*** Решение через list: ***#
# num = input('Введите цифру месяца: ')
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for res in li:
#     if num in {0, 1, 11}:
#         print(res('Зима'))
#         break
#     if num in {2, 3, 4}:
#         print(res('Весна'))
#         break
#     if num in {5, 6, 7}:
#         print(res('Лето'))
#         break
#     if num in {8, 9, 10}:
#         print(res('Осень'))
#         break
# print('Конец')

# 4 задание

# dlina = 0
# li = input().split()
# for word in li:
#     dlina += 1
#     if len(str(word)) > 10:
#         print( dlina, ".", str(word)[0:10])
#     else:
#         print( dlina, ".", word)

# 5 задание (решение подсмотрел в документациях)

# rate = [10, 10, 5, 4, 1]
# print(f"Текущий рейтинг: {rate}")
#
# new_scores_count = int(input("Какие рейтинги добавляем?: "))
#
# for i in range(1, new_scores_count + 1):
#     new_score = int(input('Введите число: '))
#     if new_score > 0:
#         rate.append(new_score)
#         rate.sort(reverse=True)
#         print(f"Новый рейтинг: {rate}")
#         break
#     else:
#         print("Ошибка, введите натуральное число.")
#         break
# print('Конец')