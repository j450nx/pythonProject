from load import load_strings

names = load_strings('names/unsorted.txt')
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
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_names = quicksort(names)
for n in sorted_names:
    print(n)