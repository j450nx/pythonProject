def is_adult(age):
    if age > 18:
      return True
    else:
      return False

# ternary operators
def is_adult2(age):
  return True if age > 18 else False

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read]) # True

ingredients_purchased = True
meal_cooked = False
read_to_serve = all([ingredients_purchased, meal_cooked]) # False

num1 = 2 + 3j
num2 = complex(2, 3)
print(num1.real, num2.imag)

print(abs(-5.5))

print(round(5.49, 1)) #round to nearest 10th digit

from enum import Enum

class State(Enum): #to create constants
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])

print(list(State))
print(len(State))

# age = input('What is your age: ')
# print(f'Your age is {age}')

condition = True
if condition == True:
    print('The condition')
    print('was true')
else:
    print('The condition')
    print('was false')

condition = False
print(condition)

# lists
dogs = ['Roger', 1, 'Syd', True, 'Quincey', 7]
print('Roger' in dogs)
print('Jason' in dogs)
print(dogs[0])
dogs[2] = 'Jason'
print(dogs)
print(dogs[-2])
print(dogs[2:4]) # slice from index 2 and stops before 4
dogs.append('Judah')
print(dogs)
dogs.extend(['item1', 5]) # same as dogs =+ ['item1', 5]
print(dogs)
dogs.remove(1)
print(dogs)
print(dogs.pop())
print(dogs)

items = ['roger', 'Syd', 'Quincey']
items.insert(2, 'Tests')
print(items)
items[1:1] = ['Test1', 'Test2']
print(items)
items.sort()
print(items)
itemscopy = items[:] # make a copy with slice
items.sort(key=str.lower) # sort without worrying about upper/lower case
print(items)
print(itemscopy)

print(sorted(itemscopy, key=str.lower)) # sort without modifying the original list
print(itemscopy)

# Tuples create immutables
names = ('Roger', 'Syd', 'Jason')
print(names[0])
print(names.index('Roger'))
print(names[-1])
print(len(names))
print('Roger' in names)
print(names[0:2])
print(sorted(names)) # sort and print new tuple
newTuple = names + ('Tina', 'Quincey')
print(newTuple)

# Dictionaries
dog = { 'name': 'Roger', 'age': 8, 'color': 'green' }
print(dog['name'])
dog['name'] = 'Syd'
print(dog['name'])
print(dog.get('name'))
print(dog.get('color', 'brown')) # default color is brown if no 'color' key is found
print(dog.pop('name')) # dog.popitem() will remove the last item of the dictionary
print(dog)
dog['name'] = 'Syd'
print(dog)
print('color' in dog)
print(list(dog.keys()))
print(dog.values())
print(list(dog.items()))
dog['favorite food'] = 'meat'
print(dog)
del dog['color']
print(dog)
dogCopy = dog.copy()

# Sets can not have two of the same item

set1 = {'Roger', 'Syd', 'Syd'}
set2 = {'Lune', 'Roger'}

intersect = set1 & set2
print(intersect)

union = set1 | set2
print(union)

difference = set1 - set2
print(difference)

print(set1 > set2) #does set1 contain all of set2?

print(list(set1))

# Functions

def hello(name='my friend', age=10): # default arguments are my friend and 10
    print(f'Hello {name}! You are {age} years old.')
hello('Jason', 30)
hello('Beau')
hello()

def change(value):
    value['name'] = 'Jason'

val = {'name': 'Jayden'} #dictionary is mutable via a function
print(val)
change(val)
print(val)

def greeting(name):
    print(f'Hello {name}!')
    return name, 'Jason', 8
print(greeting('Jason'))

# Variable scopes
age = 8
def test():
    print(age)
print(age)
test()

# nested functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count():
    count = 0
    def increment():
        nonlocal count #nonlocal to access variable outside the scope
        count = count + 1
        print(count)
    increment()
count()

# Closures
def counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()

print(increment())
print(increment())
print(increment())

# Objects - everything in Python is an object
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())
print(id(age))
age = age + 1
print(age)
print(id(age))

items = [1, 2]
items.append(3)
items.pop()
print(id(items)) # place in memory

# Loops - While and For
condition = True
while condition == True:
    print('The condition is True')
    condition = False

names = ['Jayken', 'Jaycee', 'Jayko']
for index, name in enumerate(names):
    print(index, name)

for a in range(5):
    print(a)

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break
    print(item)

#Classes
class Animal:
    def walk(self):
        print('Walking...')
#inheritence
class Dog(Animal):
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('Woof!')

roger = Dog('Roger', 8)
print(type(roger))
print(roger.name)
roger.bark()
roger.walk()

#Modules - every Python file is a module
"""
math for math utilities
re for regular express
json to work with JSON
datatime to work with dates
sqlite3 to use SQLite
os for Operating System utilities
random for random number generation
statistics for statistics utilities
requests to perform HTTP network requests
http to create HTTP servers
urllib to mange URLs
"""
from lib import dog
# from lib.dog import bark # import bark directly

dog.bark()

import math # from math import sqrt -> sqrt(4)
print(math.sqrt(4))

#Accepting Arguments
# import sys
# print(sys.argv)
# name = sys.argv[1]
# print('Hello' + name) # in console -> python main.py {name}

# import argparse
# parser = argparse.ArgumentParser(
#     description='This program prints the name of my dogs'
# )
# parser.add_argument('-c', '--color', metavar='color',
#                     required=True, choices={'red', 'yellow'}, help='the color to search for')
# args = parser.parse_args()
# print(args.color)

#Lambda Funtions
double = lambda num : num * 2
print(double(8))
multiply = lambda a, b : a * b
print(multiply(2, 3))

# map(), filter(), reduce()
numbers = [1, 2, 3]
def double(a):
    return a * 2
# or double can be the lambda function above
result = map(double, numbers)
print(list(result))

# shorter version, put lambda function right into map()
result = map(lambda a: a * 2, numbers)
print(list(result))

result = filter(lambda a: a % 2 == 0, numbers)
print(list(result))

from functools import reduce
expenses = [('Dinner', 80), ('Car repair', 120)]
sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)
print(reduce(lambda a, b: a[1] + b[1], expenses))

# Recursion
def factorial(num):
    if num == 1: return 1
    return num * factorial(num - 1)
print(factorial(3))

# Decorators - alter how a function works without modifying the function
# eg. add logging, test performance, perform caching, verify performance
def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper
@logtime
def hello():
    print('Hello')
hello()

# Docstrings """ comment block """
print(help(dog)) #generates help documentation

# Annotations
def increment(n: int) -> int: # function receives an int and returns an int
    return n + 1

count: int = 0 # specifies count is an int

# Exceptions
"""
try:
    some lines of code
except <ERROR1>:
    handler <ERROR1>
except <ERROR2>:
    handler <ERROR2>
else:
    no exceptions were raised, the code ran successfully
finally:
    do something in any case 
"""
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Can not be divided by zoro!')
finally:
    result = 1

print(result)

try:
    raise Exception('An error!')
except Exception as error:
    print(error)

class DogNotFoundException(Exception): #extends Exception
    print('inside')
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')

""" the With statement
# without With statement
filename = '/Users/flavio/test.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()

# with With statement that automatically closes file at the end
with open(filename, 'r') as file:
    content = file.read()
    print(content)
"""

"""
# Third party packages at pypi.org
pip installs packages globally for eg. pip install requests
pip install -U requests -> installs the latest package of requests
pip -uninstall requests
pip show requests
"""

# List Compressions - sometimes is preferred over loops
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

#Polymorphism
class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

# Operator Overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

print(roger > syd)

"""
__add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv__() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator
"""