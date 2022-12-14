# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Изначальный список:  " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i+1)
    list[i], list[j]=list[j], list[i]
print("Перемешанный список: " + str(list))    

# Метод 2
# from random import randrange

# num = int(input())
# nums_list = list(range(num))

# print(nums_list)

# for i in range(num):
#     n_1, n_2 = randrange(num), randrange(num)
#     nums_list[n_1],  nums_list[n_2] =  nums_list[n_2],  nums_list[n_1]
# print(nums_list)

