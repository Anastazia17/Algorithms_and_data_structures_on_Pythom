"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit

print(timeit("""def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
"""))
#Время выполнения составило: 0.050038799999999994 мс

print(timeit("""
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr[len(new_arr)] = [i]
    return new_arr
"""))
# Время выполнения составило: 0.0487888 мс

# В данном коде вместо new_arr.append(i) используется new_arr[len(new_arr)] = [i],
# что немного сокращает время выполнения функции.

# Вывод: 2-й вариант хоть немного, но все же лучше.