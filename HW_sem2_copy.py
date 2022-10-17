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

# N = int(input('N: '))
# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
    
#     print(f, end=", ")

# Задача 3. Задайте список из n чисел 
# последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

# n = int(input('Введите число N: ')) 
# list = [(1  + 1 / n) ** n for n in range (1, n  +  1)]        
# print ((sum(list)))


# Задача 4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# path = 'file.txt'
# data = open (path, 'r')
# for line in data:
#     print(line)
# data.close()

# n = int(input('N: '))
# print(*range(-n, n + 1), sep = ', ')
# Не понимаю дальше как (


# Задача 5. Реализуйте алгоритм перемешивания списка.

# from random import Random, randint
# N = int(input('Введите число ')) # ввожу количество цифр в списке
# numbers = [] # сначала список пустой
# for i in range(N):
#     numbers.append(randint(-N, N+1)) # задаю отрезок от N до -N
# print(numbers) # вывожу список на экран

# def new(numbers): # создаем новый список
#     list = numbers[:]
#     numbers_length = len(list) # длина списка
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1) # инд списка от [0] до посл
#         temp = list[i] # вводим вр переменную, чтобы перезаписывать
#         list[i] = list[index] 
#         list[index] = temp
#     return list # возвращаем список
# print(new(numbers)) # печатаем на экран нов список