def sum(numbers):
    # Base case to stop loop
    if not numbers:
        return 0
    # print('Calling sum(%s)' % numbers[1:])
    # Python call stack to keep track of the function calls
    remaining_sum = sum(numbers[1:])
    # print('Call to sub(%s) returning %d + %d' % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum([1, 2, 3, 4]))