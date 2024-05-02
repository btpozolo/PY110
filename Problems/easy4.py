# Alphabetical Numbers

'''
- list of words

'''
WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

def get_word(num):
    return (WORDS[num])

def alphabetic_number_sort(lst):
    return sorted(lst, key=get_word)
print(alphabetic_number_sort(
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# Merge Sets

def merge_sets(lst1, lst2):
    return set(lst1).union(set(lst2))

print(merge_sets([3,5,7,9], [5,7,11,13]))
# {3, 5, 7, 9, 11, 13}

# Immutable Intersection

'''
algo:
- convert both lists to frozensets
- find overlap of sets
- return frozenset of overlap
'''

def find_intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2)

print(find_intersection([2,4,6,8], [1,3,5,7,8]))
# frozenset({8})

# Arrange a dictionary
'''
algo:
- list comprehension
    - sorted (key = value)
'''

def order_by_value(dct):
    sort_list = sorted(dct.items(), key=get_value)
    return ([k for k, v in sort_list])

def get_value(item):
    return item[1]

print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']

# unique elements

'''
algo
loop through elements in first list, check if in 2nd list

alt:
check for overlapping 
'''

def unique_from_first(lst1, lst2):
    final_set = set()
    for item in set(lst1):
        if item not in set(lst2):
            final_set.add(item)
    return final_set

def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)

print(unique_from_first([3,6,9,12], [6,12,15,18]))
# {9, 3}

# leading substrings

def leading_substrings(string):
    lst = []
    for i in range(1,len(string) + 1):
        lst.append(string[:i])
    return

def leading_substrings(string):
    return([string[ : i+1] for i in range(len(string))])


print(leading_substrings('abc'))      # ['a', 'ab', 'abc']
print(leading_substrings('a'))        # ['a']
print(leading_substrings('xyzzy'))    # ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']

# All substrings

def substrings(string):
    subs = []
    for i in range(len(string)):
        subs.extend(leading_substrings(string[i:]))
    return subs

def substrings(string):
    return ([item for i in range(len(string))
             for item in leading_substrings(string[i:])])

print(substrings('abcde'))

# prints
# [ "a", "ab", "abc", "abcd", "abcde",
#  "b", "bc", "bcd", "bcde",
#  "c", "cd", "cde",
#  "d", "de",
#  "e" ]

# Palindromic Substrings

def is_palindrome(string):
    if len(string) > 1:
        midpoint = len(string) // 2

        for idx in range(midpoint):
            if string[idx] != string[-idx - 1]:
                return False
    else:
        return False
    return True

def is_palindrome(string):
    if len(string) < 2:
        return False
    
    return all([string[i] == string[-i - 1] for i in range(len(string) // 2)])

is_palindrome('AbcbA')
is_palindrome('Abcba')
is_palindrome('a')

def palindromes(string):
    subs = substrings(string)
    return ([item for item in subs if is_palindrome(item)])


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

# Inventory Items Transaction

'''
input: integer, list
oupput: list of transactions
algo:
'''

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

def transactions_for(id, transactions):
    end_lst = []
    for line in transactions:
        if line['id'] == id:
            end_lst.append(line)
    return end_lst

def transactions_for(id, transactions):
    return([line for line in transactions if line['id'] == id])

print(transactions_for(101, transactions))
# prints
# [ {"id": 101, "movement": "in",  "quantity":  5},
#   {"id": 101, "movement": "in",  "quantity": 12},
#   {"id": 101, "movement": "out", "quantity": 18} ]

# Inventory Item Availability 

'''
algo:
- get all transactions for an id
- iterate through those transactions
    - adding if in, subtracting if out
- return if value > 0 
'''

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

def is_item_available(id, transactions):
    id_lines = transactions_for(id, transactions)
    current_inv = 0
    for line in id_lines:
        direction = 1 if line['movement'] == 'in' else - 1
        current_inv += line['quantity'] * direction
    
    return current_inv > 0

def is_item_available(id, transactions):
    
    def get_direction(dct):
        return 1 if dct['movement'] == 'in' else -1
    
    current_inv = sum([t['quantity'] * get_direction(t) for t in transactions_for(id, transactions)])
    
    return current_inv > 0
print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True
