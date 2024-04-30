"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string. Palindrome detection
should be case-sensitive.
"""

'''
Input: string
Output: list of strings
Rules:
    Explicit:
         returns list of palindromes
         palindromes are case sensitive
    Implicit:
        Palindrome substrings can overlap each other
        Works for empty string
'''

# Test cases:

# Comments show expected return values
# palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
# palindrome_substrings("palindrome") # []
# palindrome_substrings("")           # []
# palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
# palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]



def create_row(start_int, row_length):
    row = []
    current_int = start_int
    while len(row) < row_length:
        row.append(current_int)
        current_int += 2

    return row

def sum_even_number_row(row_number):
    rows = []
    current_row = 1
    current_int = 2

    while len(rows) < row_number:
        new_row = create_row(current_int, current_row)
        rows.append(new_row)

        current_int = new_row[-1] + 2
        current_row += 1

    return sum(rows[-1])


print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

# print(create_row(2, 1) == [2])
# print(create_row(4, 2) == [4, 6])
# print(create_row(8, 3) == [8, 10, 12])

# Leftover Blocks
'''
Input = integer - number of blocks
Outup = integer - remaining blocks after creating tallest possible structure
Rules:
    Explicit:
        - blocks are cubes
        - built in layers
        - no gaps
        - top level is single block
    Implicit:
        - each additional level will require the max level number squared, additional blocks
Questions:
    - do we care about returning the max structure height?
    - do we always pass in a positive integer?
Data Structure:
    - list of ints (number of blocks in each layer)
Algorithm:
    - get block remaining for layers 
    - get amount of blocks needed for next layer

    - check if # of blocks remaing is enough for next layer
        - if so, add that layer
        - decrement the a remaining blocks by # in that layer
        - calculate amount of blocks needed for next layer
    - return the remaining blocks
    
'''
def calculate_leftover_blocks(blocks):
    blocks_remaining = blocks
    blocks_required = 0
    current_layer = 0

    while blocks_remaining >= blocks_required:
        blocks_remaining -= blocks_required
        current_layer += 1
        blocks_required = current_layer ** 2
    
    return blocks_remaining


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

'''
Input: List of strings
Output: List of strings
Rules
    - Explicit:
        - sorted by highest number of adjacent consonants
        - if same amount, retain original order of string
    - Implicit:
        - Strings may contain single or multiple words.
        - Strings may not be empty.
        - Strings may have no adjacent consonants.
        - Strings should be sorted in descending order.
        - Case is not relevant.
        - Single consonants in a string do not affect sort order in
        comparison to strings with no consonants. Only adjacent
        consonants affect sort order.
Questions:
- how does a space between to adjacent words work? Which one gets the consonant counts?
- how does punctuation apply? - ' etc?
- can strings be empty?
- should i sort in ascending or descending order

Data Structure:
- List of strings
- Iterate through strings while counting 

Algorithm:
- store the initial positions of each string
- count max number of adjacent consonants for each string
- save this number linked to the string
- sort strings descending based on adjacent consonants
    - leave in place if same
- return the new sorted list

Code
'''
string = "ddd daaaa"
string = string.replace(" ", "")

max_consonants = 0
adj_consonants = ""

VOWELS = set('a', 'e', 'i', 'o', 'u')

for char in string:
    if char not in VOWELS:
        adj_consonants += char
    else:
        length = len(adj_consonants)
        if length > max_consonants and length > 1:
                max_consonants = length
        adj_consonants = ""
# - Initialize a "maximum consonants count" to zero.
# - Initialize an "adjacent consonants string" to an empty string.
# - For each "letter" in the "input string":
#     - If the "letter" is a consonant:
#         - Concatenate it to the "adjacent consonants string".
#     - If the "letter" is a vowel:
#         - If the "adjacent consonants string" has a length
#           greater than the current "maximum consonants count":
#             - If the "adjacent consonants string" has a length
#               greater than 1:
#                 - Set the "maximum consonants count" to the length
#                   of the "adjacent consonants string".

#         - Reset the "adjacent consonants string" to an empty string.

# - Return the "maximum consonants count".


def count_max_adjacent_consonants(string):
    string = string.replace(" ", "")

    max_consonants = 0
    adj_consonants = ""

    VOWELS = set(['a', 'e', 'i', 'o', 'u'])

    for char in string:
        if char not in VOWELS:
            adj_consonants += char
        
        length = len(adj_consonants)
        if length > 1 and length > max_consonants:
                max_consonants = length
        if char in VOWELS:
            adj_consonants = ""
    
    return max_consonants

def count_max_adjacent_consonants(string):
    string = ''.join(string.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''
    for letter in string:
        if letter in 'bcdfghjklmnpqrstvwxyz':
            adjacent_consonants += letter
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)

            adjacent_consonants = ''

    return max_consonant_count


print(count_max_adjacent_consonants('month'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings
    
    consonant_dict = {}
    for string in strings:
        result = count_max_adjacent_consonants(string)
        consonant_dict[string] = result

    values = list(consonant_dict.values())
    values.sort(reverse=True)

    #print(consonant_dict)

    new_strings = []
    
    while values:
        for key, value in consonant_dict.items():
            if value == values[0]:
                new_strings.append(key)

                values.pop(0)
                del consonant_dict[key]
                break
    
    return new_strings

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa'] 0 adjacent consonants in aa and baa

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']


produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce):
    fruits = {}
    for key, value in produce.items():
        if produce[key] == 'Fruit':
            fruits[key] = value
    return fruits

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

def double_numbers(numbers):
    for index, num in enumerate(numbers):
        numbers[index] = num * 2
    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

def double_numbers(numbers):
    nums = []
    for index, num in enumerate(numbers):
        if index % 2 != 0:
            nums.append(num * 2)
        else:
            nums.append(num)
    return nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

def multiply(numbers, times):
    result = []
    for num in numbers:
        result.append(num * times)
    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]