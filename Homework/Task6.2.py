# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in 424
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

#1
num = int(input("Введите длину списка N: "))
def multipl_list(num: int):
    a = [i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0]
    return a
print()
print(f"Список чисел в пределах от 20 до N, кратных 20 и 21:\n {multipl_list(num)}")
print()

#2
def uniq_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]


print(uniq_list(int(input())))
