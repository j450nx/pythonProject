from timeit import default_timer as timer
from load import load_numbers

numbers = load_numbers('numbers/8.txt')
"""
Runs at O(n2) time
"""
def quicksort(values):
    # base case
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # recursive call
    # print('%15s %1s %-15s' % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


print(numbers)
start = timer()
print('Time start: ', start)
sorted_numbers = quicksort(numbers)
end = timer()
print('Time finish: ', end)
print(end-start)
print(sorted_numbers)