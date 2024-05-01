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

# Rotation Pt 1

'''
PEDAC - outline
input : list
output : new list 
rules
    explicit:
        - moves the first element to the end of the list
        - if empty return empty list
        - if input is not a list return none
    implicit:
        -  

Questions:
- 

Data Structure:
- 
Algorithm:
- check if input is a list
- check in list has any elements
- if so, create a new list
    - remove first element and append that to the end of the list

'''

def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if not lst:
        return ([])
    
    rotated_lst = list(lst)
    first_element = rotated_lst.pop(0)
    rotated_lst.append(first_element)

    return rotated_lst

def rotate_rightmost_digits(integer, num_digits):
    string = str(integer)
    end = rotate_list(list(string[-num_digits:]))
    end_str = ''
    start_str = string[:-num_digits]
    for char in end:
        end_str += str(char)

    return int(start_str + end_str)

def max_rotation(number):
    str_num = str(number)
    digits = len(str_num)

    for i in range(digits):
        number = rotate_rightmost_digits(number, digits - i)

    return number

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845

print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917

print(rotate_list([7, 3, 5, 2, 9, 1]))           # [3, 5, 2, 9, 1, 7]
print(rotate_list(['a', 'b', 'c']))              # ['b', 'c', 'a']
print(rotate_list(['a']))                        # ['a']
print(rotate_list([1, 'a', 3, 'c']))             # ['a', 3, 'c', 1]
print(rotate_list([{'a': 2}, [1, 2], 3]))       # [[1, 2], 3, {'a': 2}]
print(rotate_list([]))                           # []

# return `None` if the argument is not a list
print(rotate_list(None))                         # None
print(rotate_list(1))                            # None

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst))                    # [2, 3, 4, 1]
print(lst)                                # [1, 2, 3, 4]