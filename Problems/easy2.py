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


#1 Cute Angles

'''
PEDAC - outline
input : floating point number
output : string for that angle in degrees, minutes, and seconds
rules
    explicit:
        - use ˚ for degrees, ' for minutes and " for seconds
        - 60 minutes in a degree and 60 seconds in a minute
        - inputs range from 0 to 360 
    implicit:
        -  left of decimal = degrees
        - right of decimal * 60 gets minutes 
        - right of decimal * 60 gets seconcds

Questions:
- what is the conversion from 

Data Structure:
- 
Algorithm:
- take everything left of decimal as degrees
- right of decimal * 60, rounded down is minutes (ensure two digits)
- right of decimal of above step * 60, is seconds (ensure 2 digits)
- return formated string of above
'''

def dms(angle):
    degrees = int(angle // 1)
    minutes = angle % 1 * 60
    seconds = int(minutes % 1 * 60)
    minutes = int(minutes)

    return f"{degrees:01d}°{minutes:02d}'{seconds:02d}\""


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# 2 Combining Lists

'''
PEDAC - outline
input : two lists
output : set - containing union of values from two lists
rules
    explicit:
        - will always be given lists
    implicit:
        -  

Questions:
- 

Data Structure:
- set and union
Algorithm:
- convert both lists into sets
- union both sets
- return uninion of sets
'''
def union(list1, list2):
    combined_set = set()
    set1 = set(list1)
    set2 = set(list2)

    combined_set = set1.union(set2)

    return combined_set

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# 3 Halvsies 

'''
PEDAC - outline
input : list
output : list with 2 nested lists
rules
    explicit:
        - first half of elements in the first list 
        - if odd number - include middle in the first list
    implicit:
        -  

Questions:
- 

Data Structure:
- list
Algorithm:
- figure out if the list is even or odd
- calculate the breakpoint element number between two lists
- create two new lists via splicing
- return new list containing two sublists
'''

def halvsies(input_list):
    lst_1 = []
    lst_2 = []

    odd_num = len(input_list) % 2 != 0
    if odd_num:
        midpoint = (len(input_list) // 2) + 1
    else:
        midpoint = (len(input_list) // 2) 

    lst_1 = input_list[:midpoint]
    lst_2 = input_list[midpoint:]

    return ([lst_1, lst_2])

print(halvsies([1, 2, 3, 4, 5]))

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# 4 find duplicate
'''
PEDAC - outline
input : list
output : value
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
def find_dup(lst):
    for item in lst:
        if lst.count(item) == 2:
            return item
    return 


print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True


# Combine two lists
def interleave(lst1, lst2):
    combined = []
    for index in range(len(lst1)):
        combined.append(lst1[index])
        combined.append(lst2[index])
    
    return combined

def interleave(lst1, lst2):
    combined = []
    tup = zip(lst1, lst2)

    for a, b in tup:
        combined.append(a)
        combined.append(b)
    
    return combined


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

print(interleave(list1, list2))

# mutiplicative average
'''
PEDAC - outline
input : list of integers
output : string - rounded to 3 decimal places
rules
    explicit:
        - multiplies integers together 
        - divides the result by number of entries 
    implicit:
        -  

Questions:
- 

Data Structure:
- floats and ints 
Algorithm:
- 
'''
def multiplicative_average(lst):
    product = 1 

    for num in lst:
        product *= num

    product /= len(lst)
    return f'{product:.3f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# Multiply Lists
'''
PEDAC - outline
input : two lists of numbers
output : list of numbers
rules
    explicit:
        - each element should be the product of the other two lists
        - can assume same number of elements
    implicit:
        -  

Questions:
- can we assume no null lists

Data Structure:
- list
Algorithm:
- iterate through the length of either list
- multiple elements at that position 
- append to new list
- return new list
'''

def multiply_list(lst1, lst2):
    combined_lst = []
    for index in range(len(lst1)):
        combined_lst.append(lst1[index] * lst2[index])
    return combined_lst


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# List of Digits
'''
PEDAC - outline
input : positive integer
output : list of digits in the number
rules
    explicit:
        - 
    implicit:
        - duplicate digits are okay
        - list should have same len as num of digits in number 

Questions:
- 

Data Structure:
- string iteration
Algorithm:
- convert int to string
- iterate through string
    - converting each char into an int
    - add that int into a list
- returning list
'''

def digit_list(number):
    lst = []
    string = str(number)

    for char in string:
        lst.append(int(char))

    return lst

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# How Many
'''
PEDAC - outline
input : list 
output : printed each element alongside the number of occurances, return none
rules
    explicit:
        - case sensitive match
        - prints can be in any order
    implicit:
        -  

Questions:
- 

Data Structure:
- set to dedup
Algorithm:
- convert list to set for unique items
- iterate through set items, counting number of item in list
- print each item
'''

def count_occurrences(lst):
    unique_elements = set(lst)

    for item in unique_elements:
        print(f'{item} => {lst.count(item)}')
    return

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# List Average

'''
PEDAC - outline
input : list of integers
output : integer
rules
    explicit:
        - integers will always be positive 
    implicit:
        -  

Questions:
- 

Data Structure:
- 
Algorithm:
- sum all elements
- use integer division by len of list
'''
def average(lst):
    return(sum(lst) // len(lst))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True