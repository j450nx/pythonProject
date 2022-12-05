import random
import time

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint - 1], target)


length = 10000
# build a sorted list to length 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print('Naive search time: ', (end - start) / length, ' seconds')

start = time.time()
for target in sorted_list:
    recursive_binary_search(sorted_list, target)
end = time.time()
print('Binary search time: ', (end - start) / length, ' seconds')