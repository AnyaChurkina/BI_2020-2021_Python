import numpy as np
import time
import matplotlib.pyplot as plt
from random import shuffle


#  Sorting without Sort and Sorted (спасибо дискретной математике!)
def bubble_sort(lst):
    list_length = len(lst)
    it_is_sort = True
    res = 0
    while it_is_sort:
        it_is_sort = False
        res += 1
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                it_is_sort = True
        list_length -= 1
    res -= 1
    return lst


#  Monkey sort(script from Wiki)
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def monkey_sort(lst):
    while not is_sorted(lst):
        shuffle(lst)
    return lst


bubble_mean_time = []
monkey_mean_time = []
default_mean_time = []

bubble_sort_sd = []
monkey_sort_sd = []
default_sort_sd = []

array_size = range(1, 11)  # define size of arrays

for size in array_size:
    #  Counting mean and std for bubble sorting method
    bubble_sort_time = []
    for replication in range(6):  # define number of replication
        array = list(np.random.uniform(0, 1, size))

        start_bubble_sort_time = time.time()
        bubble_sort(array)
        bubble_sort_time.append(time.time() - start_bubble_sort_time)
    bubble_sort_sd.append(np.std(bubble_sort_time))
    bubble_mean_time.append(np.mean(bubble_sort_time))

    #  Counting mean and std for monkey sorting method
    monkey_sort_time = []
    for replication in range(6):
        array = list(np.random.uniform(0, 1, size))

        start_monkey_time = time.time()
        monkey_sort(array)
        monkey_sort_time.append(time.time() - start_monkey_time)
    monkey_sort_sd.append(np.std(monkey_sort_time))
    monkey_mean_time.append(np.mean(monkey_sort_time))

    #  Counting mean and std for default sorting method
    sort_time = []
    for replication in range(6):
        array = list(np.random.uniform(0, 1, size))

        start_sorting_time = time.time()
        sorted(array)
        sort_time.append(time.time() - start_sorting_time)
    default_sort_sd.append(np.std(sort_time))
    default_mean_time.append(np.mean(sort_time))

plt.figure(figsize=(15, 10))
plt.errorbar(array_size, bubble_mean_time, bubble_sort_sd, color="green",
             marker='s', linestyle="", label="Bubble sort")
plt.errorbar(array_size, monkey_mean_time, monkey_sort_sd, color="black",
             marker='*', linestyle="", label="Monkey sort")
plt.errorbar(array_size, default_mean_time, default_sort_sd, color="red",
             marker='o', linestyle="", label="Default sort")
plt.ylabel('Time(s)')
plt.xlabel('Array size')
plt.legend(loc='upper left')
plt.grid(alpha=.5)
plt.title("Sorting time for Monkey, Bubble, Default sort")
plt.savefig('Sorting plot Monkey-Bubble-Sorted.png')
plt.close()

#   Сравнение Bubble sort и стандартного sorted
plt.figure(figsize=(15, 10))
plt.errorbar(array_size, bubble_mean_time, bubble_sort_sd, color="green",
             marker='P', linestyle="", label="Bubble sort")
plt.errorbar(array_size, default_mean_time, default_sort_sd, color="red",
             marker='v', linestyle="", label="Default sort")
plt.ylabel('Time(s)')
plt.xlabel('Array size')
plt.legend(loc='upper left')
plt.grid(alpha=.5)
plt.title("Sorting time for Bubble and Default sort")
plt.savefig('Sorting plot Bubble-Sorted.png')
