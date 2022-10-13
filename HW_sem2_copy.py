# Задача 1. Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

# print(sum(map(int, input('Введите число: ')))) # только для целых чисел!!!

# number = float(input('Введите число: '))
# str_number = str(number) #записываем число в строку
# str_number = str_number.replace('.', '') #десятичный разделитель убираем
# lst_str = list(str_number) # преобразуем число в список с цифрами
# lst_num = map(int, lst_str) # преобразуем в целые числа
# result = sum(lst_num)
# print(result)

# Задача 2. Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# т.е. 1 2 3 4 
# не понимаю как написать программу (())
# n = int(input('Введите N: '))
# def select(f, col):
#     return [f(x) for x in col]
# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4'.split()
# res = select(int, data)
# res = where(lambda x: x, res)
# res = select(lambda x: x, factorial(x))
# print(res)




# Задача 3. Задайте список из n чисел 
# последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037


# n = int(input('Введите число N: ')) 
# list = [(1  + 1 / n) ** n for n in range (1, n  +  1)]        
# print ((sum(list)))