# Searching 101

nums = ['1st', '2nd', '3rd', '4th', '5th', 'last']
input_nums = []

for num in nums:
    input_nums.append(int(input(f'Enter the {num} number: ')))

appears = 'is' if input_nums[-1] in input_nums[:-1] else "isn't"

print(f'{input_nums[-1]} {appears} in {",".join(input_nums[:-1])}.')


nums[-1:]

# Is palindrome

def is_palindrome(string):
    return string == string[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# Is real palindrome
def is_real_palindrome(string):
    new_str = ""
    for char in string:
        if char.isalnum():
            new_str += char

    new_str = new_str.lower()
    return (new_str == new_str[::-1])

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Running Totals
def running_total(nums):
    total = []
    run_total = 0
    for num in nums:
        run_total += num
        total.append(run_total)
    return total

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# Letter Counter

def word_sizes(string):
    l1 = string.split()
    my_dict = dict()

    for word in l1:
        length = len(word)

        if my_dict.get(length):
            my_dict[length] += 1
        else:
            my_dict[length] = 1
    
    return my_dict


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# Letter counter pt 2

def word_sizes(string):
    words = string.split()
    my_dict = dict()

    def remove_non_alpha(string):
        clean_str = ""
        for char in string:
            if char.isalpha():
                clean_str += char
        return clean_str


    for word in words:
        clean_word = remove_non_alpha(word)
        length = len(clean_word)

        if my_dict.get(length):
            my_dict[length] += 1
        else:
            my_dict[length] = 1
    
    return my_dict


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Letter Swap

def swap(sentence):
    words = sentence.split()
    swapped = []

    for word in words:
        # Get first and last chars
        first_char = word[0]
        last_char = ""
        if word[1:]:
            last_char = word[1:][-1]

        # remove first and last chars (splice)
        middle = word[1:len(word)-1]

        # concat word with first and last swapped
        swap = last_char + middle + first_char
        swapped.append(swap)

    return " ".join(swapped)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# Convert a string to a Number

def string_to_integer(number):
    digits = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    value = 0
    multiple = 1
    sign = 1
    
    if not number[0].isalpha():
        sign = (-1 if number.pop(0) == '-' else 1)


    for char in number[::-1]:
        value += digits[char] * multiple
        multiple *= 10

    return (value * sign)

print(string_to_integer('432543'))

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# convert a string to signed number 

def string_to_signed_integer(number):
    digits = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    value = 0
    multiple = 1
    sign = 1
    
    if number[0] in ('-', '+'):
        sign = (-1 if number[0] == '-' else 1)
        number = number[1:]


    for char in number[::-1]:
        value += digits[char] * multiple
        multiple *= 10

    return (value * sign)

print(string_to_signed_integer("4321"))

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# convert number to a string
'''
PEDAC - outline
input : integer
output : string
rules:
    explicit:
        - non-negative integer
        - may not use standard conversion functions such as str
    implicit:
        -   

Questions:
- 
Data Structure:
- dict key of numbers to strings

Algorithm:
- for each value in integer pull the string value from dict
- append that value onto a string
- return that string
'''

def integer_to_string(integer):
    string = ""
    nums = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    while integer / 10 > 0:
        last_value = integer % 10
        string = nums[last_value] + string
        integer = integer // 10 

    return string or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# Convert a signed number to a string

'''
PEDAC - outline
input :
output :
rules
    explicit:
        -
    implicit:
        -  

Questions:
- 

Data Structure:
- 
Algorithm:
- 
'''


def signed_integer_to_string(integer):
    string = ""
    nums = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    unsigned_int = abs(integer)    

    while unsigned_int / 10 > 0:
        last_value = unsigned_int % 10
        string = nums[last_value] + string
        unsigned_int = unsigned_int // 10 

    if integer < 0:
        unsigned_int *= -1
        string = '-' + string
    elif integer > 0:
        string = '+' + string

    return string or '0'


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True






'''
PEDAC - outline
input :
output :
rules
    explicit:
        -
    implicit:
        -  

Questions:
- 

Data Structure:
- 
Algorithm:
- 
'''