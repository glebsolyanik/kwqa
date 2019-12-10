'''     Task 3
    Пользователь вводит месяц в виде
    целого числа от 1 до 12.
    Сообщить к какому времени года относится месяц
    (зима, весна, лето, осень). Напишите решения через
    list и через dict.'''

month = int(input("Введите месяц(числом): "))



list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

if month in list[0]:
    month = 0
elif month in list[1]:
    month = 1
elif month in list[2]:
    month = 2
else:
    month = 3

dict = {0:    'Winter',
        1:    'Spring',
        2:    'Summer',
        3:    'Autumn',
        }

print(dict.get(month))
