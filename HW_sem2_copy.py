# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

# print(sum(map(int, input('Введите число: ')))) # только для целых чисел!!!


number = float(input('Введите число: '))
str_number = str(number) #записываем число в строку
str_number = str_number.replace('.', '') #десятичный разделитель убираем
lst_str = list(str_number) # преобразуем число в список с цифрами
lst_num = map(int, lst_str) # преобразуем в целые числа
result = sum(lst_num)
print(result)