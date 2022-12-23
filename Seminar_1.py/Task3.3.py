# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in ->88  out -> 1011000
# in ->11  out -> 1011

n = int(input("Введите десятичное число: "))
num_list = []

while n != 0:
    num_list.append(n % 2)
    n //= 2
num_list.reverse()
print(f"Преобразованное десятичное число в двоичное: {num_list}")

# Введите десятичное число: 11
# Преобразованное десятичное число в двоичное: [1, 0, 1, 1]


