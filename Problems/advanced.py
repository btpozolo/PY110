# Transpose 3x3 matrix

''''
problem
- inputs: nested lists (3x3)
- outputs: nested list (3x3) transposed (flip rows and columns)
- rules don't modify original matrix
-Example:
    [1, 5, 8],          
    [4, 7, 2],  
    [3, 9, 6],
        
        into

    1  4  3
    5  7  9
    8  2  6     

algo:
 - build a row
 - stack the rows
'''

def transpose(matrix):
    def build_row(num):
        return [matrix[0][num], matrix[1][num], matrix[2][num]]

    return [build_row(0), build_row(1), build_row(2)]

def transpose(matrix):
    return [[sub[i] for sub in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)


print(new_matrix)
print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

test = {1, 2}
print(type(test))

# Transpose n x m matrix

''''
[1]
[2]
[3]

[1, 2, 3]

'''

def transpose(matrix):
    new_num_cols = len(matrix)  # 3
    new_num_rows = len(matrix[0]) # 1

    transposed = []

    for row in range(new_num_rows):
        transposed.append([matrix[i][row] for i in range(new_num_cols)])

    return transposed

print(transpose([[1, 2, 3, 4]]))            # [[1], [2], [3], [4]]
print(transpose([[1], [2], [3], [4]]))      # [[1, 2, 3, 4]]
print(transpose([[1]]))                     # [[1]]

print(transpose([[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [3, 7, 8, 6, 2]]))
# [[1, 4, 3], [2, 3, 7], [3, 2, 8], [4, 1, 6], [5, 0, 2]]

# Rotate 90

'''
[[5, 2]]

[5]
[2]
'''

def rotate90(matrix):
    rotated = []   
    
    new_rows = len(matrix[0])

    for _ in range(new_rows):
        rotated.append([])
    
    for old_row in matrix:
        for old_col_idx, item in enumerate(old_row):
            rotated[old_col_idx].insert(0, item)
    
    return rotated


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]


print(rotate90(matrix2))

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

# Merge sorted lists

'''
algo:
- 2 pointers one for each list
- compare value at pointers 0,0 
- the smaller one append to new list and increment pointer
- if pointer at larger length, append remaining values for other list 

'''
def merge(lst1, lst2):
    pointer1, pointer2 = 0, 0
    max_1, max_2 = len(lst1), len(lst2)
    
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    sorted_lst = []
    while True:
        if lst1[pointer1] <= lst2[pointer2]:
            sorted_lst.append(lst1[pointer1])
            pointer1 += 1
        else:
            sorted_lst.append(lst2[pointer2])
            pointer2 += 1
        if pointer1 == max_1 or pointer2 == max_2:
            break
    if pointer1 < max_1:
        sorted_lst.extend(lst1[pointer1:])
    else:
        sorted_lst.extend(lst2[pointer2:])

    return sorted_lst


print(merge([1, 5, 9], [2, 6, 8]))      # [1, 2, 5, 6, 8, 9]
print(merge([1, 1, 3], [2, 2]))         # [1, 1, 2, 2, 3]
print(merge([], [1, 4, 5]))             # [1, 4, 5]
print(merge([1, 4, 5], []))             # [1, 4, 5]


# Merge Sort
'''
[9, 5, 7, 1] -->
[[9, 5], [7, 1]] -->
[[[9], [5]], [[7], [1]]]

[[[9], [5]], [[7], [1]]] -->
[[5, 9], [1, 7]] -->
[1, 5, 7, 9]

algo:
- take a list and divide into 2 lists (len // 2)
- repeat until new lists have a len of 1
- then merge and combine each with the next
    - use pointers here to keep track of position
- return final list
'''

def split_lst(lst):
        if len(lst) == 1:
            return lst
        midpoint = len(lst) // 2 
        return [split_lst(lst[:midpoint]), split_lst(lst[midpoint:])]
        
def combine_list(lst):
    new_lst =[]
    if not any([isinstance(item, list) for item in lst]):
        return lst
    else:
        # handle odds
        # handle evens
        for index in range(1, len(lst), 2):
            new_lst.extend(merge(lst[index], lst[index + 1]))
    return new_lst

print(combine_list([[[1],[2]], [[3], [4]]]))

def num_splits(number):
    splits = 0
    while 2 ** splits < number:
        splits += 1
    return splits

print(num_splits(1))
print(num_splits(2))
print(num_splits(16))
print(num_splits(17))

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    sublist_1 = lst[ : len(lst) // 2]
    sublist_2 = lst[len(lst) // 2 : ]

    print(f'sublist 1 = {sublist_1}')
    print(f'sublist 2 = {sublist_2}')

    sublist_1 = merge_sort(sublist_1)
    sublist_2 = merge_sort(sublist_2)

    return merge(sublist_1, sublist_2)

print(merge_sort([9, 5, 7, 1]))           # [1, 5, 7, 9]
print(merge_sort([5, 3]))                 # [3, 5]
print(merge_sort([6, 2, 7, 1, 4]))        # [1, 2, 4, 6, 7]

print(merge_sort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']))
# ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

print(merge_sort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]))
# [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]

# Binary Search
'''
problem - ability to cut in half and check value
input: item and list
output: index of item or = -1 if not in list
algo:
- pull middle value
- check if value is >, =, or <
- keep that part of this list
- repeat until len of list is len 1 (?)

'''
def binary_search(lst, target):
    temp_list = []
    sublist = lst
    found_target = False

    while len(sublist) > 1:

        midpoint = len(sublist) // 2
        if sublist[midpoint] == target:
            temp_list.extend(sublist[:midpoint])
            found_target = True
            break 
        elif sublist[midpoint] < target:
            temp_list.extend(sublist[:midpoint])
            sublist = sublist[midpoint:]
        else:
            sublist = sublist[:midpoint]

    if len(sublist) == 1 and sublist[0] == target:
        found_target = True
    
    return len(temp_list) if found_target else -1
    

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']

print(binary_search(businesses, 'Pizzeria'))

print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)

# Egyptian Fractions

from fractions import Fraction

print(float(Fraction(3,2)))
'''
input = a fraction
output = list of egyptian denominators
algo:
- take the biggest fraction you can away,
- continue doing this until equals sum
'''
# convert to egyptian denominators

def egyptian(fraction):
    denominators =[]
    value = 1
    current_value = fraction

    while current_value != 0:
        if Fraction(1, value) <= current_value:
            current_value -= Fraction(1, value)
            denominators.append(value)
        value += 1
    return (denominators)

def unegyptian(lst):
    value = 0
    for fraction in lst:
        value += Fraction(1, fraction)
    return value

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))