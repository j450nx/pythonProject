from timeit import default_timer as timer
from load import load_numbers

numbers = load_numbers('numbers/8.txt')
"""
Runs at O(n2) time
"""
def selection_sort(values):
    sorted_list = []
    # print('%-25s %-25s' % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        # print('%-25s %-25s' % (values, sorted_list))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


print(numbers)
start = timer()
print('Time start: ', start)
sorted_numbers = selection_sort(numbers)
end = timer()
print('Time finish: ', end)
print(end-start)
print(sorted_numbers)