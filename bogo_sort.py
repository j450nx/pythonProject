from timeit import default_timer as timer
import random
from load import load_numbers

numbers = load_numbers('numbers/8.txt')

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        # print(attempts)
        random.shuffle(values)
        # attempts += 1
    return values


print(numbers)
start = timer()
print('Time start: ', start)
sorted_numbers = bogo_sort(numbers)
end = timer()
print('Time finish: ', end)
print(end-start)
print(sorted_numbers)