import random


def my_sort(array) -> list:
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        else:
            return array[::-1]
    median = len(array) - 1
    array[median], array[len(array) // 2] = array[len(array) // 2], array[median]
    max_ind = 0
    min_ind = median - 1
    while min_ind > max_ind:
        while array[max_ind] <= array[median] and max_ind < median:
            max_ind += 1
        while array[min_ind] > array[median] and min_ind > 0:
            min_ind -= 1
        if min_ind > max_ind:
            array[min_ind], array[max_ind] = array[max_ind], array[min_ind]
    array[median], array[max_ind] = array[max_ind], array[median]
    median = max_ind
    array1 = []
    array2 = []
    if median > 0:
        array1 = my_sort(array[:median])
    if median + 1 < len(array):
        array2 = my_sort(array[median + 1 :])
    return array1 + [array[median]] + array2


a = []
n = 20
for i in range(n):
    a.append(random.randint(0, 10000))
sorted_array = a.copy()
sorted_array.sort()
print(a)
my_array = my_sort(a)
print(my_array)
print(my_array == sorted_array)
