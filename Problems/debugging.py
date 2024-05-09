'''
PEDAC - process

Problem:
    - Input:
    - Output:
Rules:
    - Explicit:
    - Implicit:
Examples / Test Cases:
Data Structure:
Algorithm:
Code: with intent
'''

# countdown

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

# Example 

bools = [True, False, True]
nums = [1, 2, 3]

for bool in bools:
    bool = nums.pop() # this doesnt mutate the bools list

print(bools) # prints [True, False, True]

bools = [True, False, True]
nums = [1, 2, 3]

for indx, _ in enumerate(bools): # is there a way to do something like this without enumerate?
    bools[indx] = nums.pop() # this does mutate bools

print(bools) # prints [True, False, True]

# Reverse String


def reverse_string(s):
    s1 = ''
    for char in s:
        s1 = char + s1
    return s1

print(reverse_string("hello"))

# Multiply List

def multiply_list(lst):
    for index, item in enumerate(lst):
        lst[index] *= 2
    return lst

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]))

def multiply_list(lst):
    doubled_lst =[]
    for item in lst:
        doubled_lst.append(item * 2)
    return doubled_lst

print(multiply_list([1, 2, 3]))

# Key Check

def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"b": 1}, "b"))

# Calendar Event Checker

'''
algo:
- 
'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"]
}

def is_date_available(date):
    if date in events:
        return False
    return True

def is_date_available(date):
    return date not in events

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

# Mutable Defaul Arguments

def append_to_list(value, lst=[]):
    lst = []
    lst.append(value)
    return lst

print(append_to_list(1))        # Expected: [1]
print(append_to_list(2))        # Expected: [2]


def sum_by_factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_by_factor(numbers, 2) == 20)

# Copy issues

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0])  # Expected: [1]

# Set Modifications

data_set = {1, 2, 3, 4, 5}

for item in tuple(data_set):
    if item % 2 == 0:
        data_set.remove(item)

data_set = {item for item in data_set if item % 2 != 0}

print(data_set)

# list deduplication

data = [ 2, 3, 2, 4, 3, 1, 1]
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

#unique_data = list(set(data))
print(unique_data)  # The order is not guaranteed to be [1, 2, 3, 4]
