# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int (input("Введите первую координату x: "))
y = int (input("Введите вторую координату y: "))
if x == 0 or y == 0:
    print("Ошибка! Введите значение больше 0")
if x > 0 and y > 0:    
    print("1")
elif x < 0 and y > 0:  # x < 0 < y
     print("2")
elif x < 0 and y < 0:  
     print("3")
elif x > 0 and y < 0:  # x > 0 > y 
     print("4")
# else:
# print("Error, 0 entered!") вместо первого условия

