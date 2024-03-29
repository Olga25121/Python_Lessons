# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in -> 4   out ->[2, 5, 8, 10]  [20, 40]
# in -> 5   out ->[2, 2, 4, 8, 8]  [16, 16, 4]

# from random import randint

# num = int(input("Введите длину списка: "))
# num_list = []

#     num_list.append(randint (1, 10))
#     if len(num_list) % 2 != 0:
#         pair_list = len(num_list)//2 + 1
#     else:
#         len(num_list)//2
#     pair_list = [num_list[i]*num_list[len(num_list)-i -1]]
#     print(pair_list)
# print(num_list)

#1
import random

n = int(input("Введите длину списка: "))
num_list = [random.randint(1, 10) for i in range(n)]


def multiple_nums(element):
    pair_list = []
    for i in range((len(element) + 1) // 2):
        pair_list.append(element[i] * element[len(element) - 1 - i])
    return pair_list

print(num_list, end=" =>")
print(multiple_nums(num_list))

# [6, 6, 7, 8] =>[48, 42]

#2
from random import sample


def list_rand_nums(count):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(prod_pairs(all_list))