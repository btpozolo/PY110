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

# After midnight

'''
PEDAC - outline
input : integer - num of mins relative to midnight
output : string - 24 hour time
rules
    explicit:
        - cant use datetime module
    implicit:
        -  

Questions:
- 

Data Structure:
- 
Algorithm:
- convert to positive numbers - and save if negative
- get number of times integer divides into 60
- get remainder from that division
- combined the two to midnight based on int sign
- handle 60 and 24 based of hours and minutes
- need to integer divide hours by 24 to hold the clock
- format string
'''

def time_of_day(number):
    is_negative = number < 0 
    number = abs(number)

    hours, minutes = divmod(number, 60)

    if is_negative:
        minutes = 60 - minutes
        hours = 24 - hours - (1 if minutes else 0)

    hours = hours % 24 

    return (f'{hours:02d}:{minutes:02d}')

print(time_of_day(3000))

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Part two 

'''
algo:
- parse string
- convert hours to minutes relative to midnight
- combine with minutes
- subtract or add from midnight
'''

HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

def after_midnight(string):
    hours, minutes = [int(num) for num in string.split(':')]

    hours *= MINUTES_IN_HOUR
    total_min = hours + minutes
    total_min = total_min % MINUTES_IN_DAY    

    return total_min

def before_midnight(string):
    hours, minutes = [int(num) for num in string.split(':')]

    hours *= MINUTES_IN_HOUR
    total_min = MINUTES_IN_DAY - (hours + minutes)
    total_min = total_min % MINUTES_IN_DAY    

    return total_min

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# double char

'''
algo:
- loops through strings char
- duplicates character 
- adds to new string
'''

def repeater(string):
    new_string = ''

    for char in string:
        new_string += (char * 2)

    return new_string

def repeater(string):
    return ''.join([char * 2 for char in string])

print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""

# Double char part 2


'''
algo:
- create a string of vowel
- for each char, checks if alpha and not vowl
- if so double and append to string
- other wise append to string
'''

def double_consonants(string):
    VOWELS = 'aeiouAEIOU'

    new_str = ''

    for char in string:
        if (char not in VOWELS) and (char.isalpha()):
            new_str += (char * 2)
        else:
            new_str += char
    return new_str

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# Reverse Number
'''
algo:
- convert number to string
- reverse string
- conver back to int
'''

def reverse_number(number):
    return int(str(number)[::-1])

print(reverse_number(12345))    # 54321
print(reverse_number(12213))    # 31221
print(reverse_number(456))      # 654
print(reverse_number(12000))    # 21 # Note that leading zeros in the result get dropped!
print(reverse_number(1))        # 1

# counting up

'''
algo:
- 
'''

def sequence(number):
    return list(range(1, number + 1))

print(sequence(5))    # [1, 2, 3, 4, 5]
print(sequence(3))    # [1, 2, 3]
print(sequence(1))    # [1]

# Name swapping

'''
algo:
- split string into list
- return list in rev order
'''

def swap_name(name):
    lst = name.split()
    rev = ', '.join(lst[::-1])
    return rev

print(swap_name('Joe Roberts'))    # "Roberts, Joe"

# Sequence Count

def sequence(count, start_num):
    lst = []
    for i in range(1, count + 1):
        lst.append(start_num * i)
    return lst

print(sequence(5, 1))          # [1, 2, 3, 4, 5] =
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []

# Reversed lists

'''
algo:
- get len of list
- iterate through len of string 
- pop first element and put it at - index of loop on
- return list
'''

def reverse_list(lst):
    temp_lst = lst[::-1]
    for i in range(len(lst)):
        lst[i] = temp_lst[i]
    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True

# Matching Parenthesis

'''
algo:
- find leftmost )
- find the next ( to the left of that spot
    - if can't return false
- remove both 
- repeat above steps until no matches remain

'''

string =  "What ((is))) up("
inner_right = string.find(')')
inner_left = string[:9].rfind('(')

inner_right = string[inner_right:].find(')') + inner_right
string.count(')')

def is_balanced(s):
    paren = 0
    for char in s:
        if char == '(':
            paren += 1
        elif char == ')':
            paren -= 1
        if paren < 0:
            return False
    return paren == 0

print(is_balanced('hi) is this ('))