#1 

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))
print(sorted(lst,reverse=True))

#2
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

#3
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst)

lst.sort(reverse=True, key=str)
print(lst)

#4

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {   'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def get_pub_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_pub_year)
print(sorted_books)

# 1

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print([key for key in dict2['3rd'].keys()][0])

dict2['3rd'].items()
for item in dict2.keys():
    print(item)

#2 

lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2)

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2)

#3
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

print(f'a = {a}\nb = {b}') # a = 2, b = [3, 8]

#4

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

print(munsters['Herman']['age'])

for n in munsters:
    print(f"{n} is a {munsters[n]['age']}-year-old {munsters[n]['gender']}.")

'''
Herman is a 32-year-old male.
Lily is a 30-year-old female.
Grandpa is a 402-year-old male.
Eddie is a 10-year-old male.
Marilyn is a 23-year-old female.
'''

## Comprehensions

#1
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

age = 0
for name, info in munsters.items():
    print(name, info)
    if info['gender'] == 'male':
        age += info['age']
print(age)

print(sum([info['age'] for name, info in munsters.items() if info['gender'] == 'male']))

#2

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []

for sublist in lst:
    new_lst.append([])
    for item in sublist:
        new_lst[-1].append(item)
    new_lst[-1].sort()

print(new_lst)    

print([sorted(sublist) for sublist in lst])

[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

#3 

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for sublist in lst:
    new_lst.append(sorted(sublist, key=str))

new_lst = [sorted(sublist, key=str) for sublist in lst]

print(new_lst)

[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

#4

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dct = dict()
for key, value in lst:
    dct[key] = value
print(dct)

dct = {key:value for key, value in lst}
print(dct)
# Pretty printed for clarity
{
    a: 1,
    b: 'two',
    sea: {c: 3},
    D: ['a', 'b', 'c']
}

#5


lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(lst):
    return sum([item for item in lst if item % 2 != 0])

print(sorted(lst, key=sum_odds))
# works

#6 

def increment_values(dct):
    return {key : value + 1 for key, value in dct.items()}

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_lst = [increment_values(dct) for dct in lst]
print(new_lst)

#7

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def mult_3(lst):
    return [item for item in lst if item % 3 == 0]

new_lst = [mult_3(sublist) for sublist in lst]
print(new_lst)

new_lst = []
for sublist in lst:
    new_lst.append([])
    for item in sublist:
        if item % 3 ==0:
            new_lst[-1].append(item)
print(new_lst)

[[], [3, 12], [9], [15, 18]]

#8
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_info(dct):
    match dct['type']:
        case 'fruit':
            value = [color.capitalize() for color in dct['colors']]
        case 'vegetable':
            value = dct['size'].upper()
    return value

new_lst = [get_info(item) for item in dict1.values()]
print(new_lst)

#9
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Checks list for all even
def even_values(lst):
    for item in lst:
        if item % 2 != 0:
            return False
    return True

def even_dict(dct):
    for key, value in dct.items():
        if not even_values(value):
            return False
    return True

print([dct for dct in lst if even_dict(dct)])


import random as r

def uuid_creator():
    string = ''
    AVAILABLE_CHARS = '0123456789abcdef'

    def get_chars(num_chars):
        string = ''
        for i in range(num_chars):
            string += r.choice(AVAILABLE_CHARS)
        return string
    return f'{get_chars(8)}-{get_chars(4)}-{get_chars(4)}-{get_chars(4)}-{get_chars(12)}'


uuid_creator()

#11

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []
VOWELS = 'aeiou'
for lst in dict1.values():
    for word in lst:
        for char in word:
            if char in VOWELS:
                list_of_vowels.append(char)

list_of_vowels = [char for lst in dict1.values() 
                for word in lst
                for char in word
                if char in VOWELS]


print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']