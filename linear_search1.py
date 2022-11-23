from load import load_strings
import names

names = load_strings('names/unsorted.txt')
search_names = ['this', 'on', 'that', 'and', 'of', 'the'];

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None

for n in search_names:
    index = index_of_item(names, n)
    print(index)

