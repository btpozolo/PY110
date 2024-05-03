# Inverting Dictionary

def invert_dict(dct):
    return {value : key for key , value in dct.items()}

print(invert_dict({'apple': 'fruit', 'broccoli': 'vegetable', 'salmon': 'fish'}))
# {'fruit': 'apple', 'vegetable': 'broccoli', 'fish': 'salmon'}

# Retain specific keys

def keep_keys(dct, lst):
    return {k : v for k, v in dct.items() if k in lst}

print(keep_keys({'red': 1, 'green': 2, 'blue': 3, 'yellow': 4}, ['red', 'blue']))
# {'red': 1, 'blue': 3}

# Delete Vowels
VOWELS = 'aeiouAEIOU'
def remove_vowels(lst_strings):
    new_lst = []
    for word in lst_strings:
        new_word = ''
        for char in word:
            if char not in VOWELS:
                new_word += char
        new_lst.append(new_word)
    return new_lst


print(remove_vowels(['abcdefghijklmnopqrstuvwxyz']))        # ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(['green', 'YELLOW', 'black', 'white'])) # ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(['ABC', 'AEIOU', 'XYZ']))               # ['BC', '', 'XYZ']

# how long are you

'''
algo:
- split strings into words
- count and append length int to word
- do this for all words in list
- return list
'''

def append_len(word):
    return " ".join([word, str(len(word))])

def word_lengths(sentence=''):
    if not sentence:
        return []
    return([append_len(word) for word in sentence.split()])

print(word_lengths('cow sheep chicken'))
# ['cow 3', 'sheep 5', 'chicken 7']

print(word_lengths('baseball hot dogs and apple pie'))
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

print(word_lengths("It ain't easy, is it?"))
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

print(word_lengths('Supercalifragilisticexpialidocious'))
# ['Supercalifragilisticexpialidocious 34']

print(word_lengths(''))      # []
print(word_lengths())        # []

print(append_len('pig'))

# List Element Multiplication

'''
algo:
- 
'''

def multiply_elements(lst1, lst2):
    return([lst1[i] * lst2[i] for i in range(len(lst1))])

print(multiply_elements([1, 2, 3], [4, 5, 6]))
# [4, 10, 18]

# Sum of Sums

'''
input - list of ints
output - int
algo:
- loop through each leading sequence 
- appending the sum to a total
- return that total
'''
def sum_of_sums(numbers):
    total = 0
    for i in range(1, len(numbers) + 1):
        total += sum(numbers[:i])

    return total

def sum_of_sums(numbers):
    return sum([sum(numbers[:i]) for i in range(1, len(numbers) + 1)])

print(sum_of_sums([3, 5, 2]))        # (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3]))     # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4]))              # 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # 35

# Sum of Digits

'''
algo:
- convert int to string
- loop through chars
- convert to int and add to total
- return total
'''

def sum_digits(number):
    string = str(number)

    total = 0
    for digit in string:
        total += int(digit)
    return total

def sum_digits(number):
    return sum([int(digit) for digit in str(number)])

print(sum_digits(23))           # 5
print(sum_digits(496))          # 19
print(sum_digits(123456789))    # 45

# Staggered Case #1

'''
algo:
- create counter for upper lower
- loop through chars
- if alpha
    - set to upper / lower based on counter
- append all to string
'''

def staggered_case(sentence):
    cap = True
    new_str = ''
    for char in sentence:
        if char.isalpha():
            if cap:
                new_str += char.upper()
            else:
                new_str += char.lower()
        else:
            new_str += char
        cap = not cap
    return new_str

print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"

#2

def staggered_case(sentence):
    cap = True
    new_str = ''
    for char in sentence:
        if char.isalpha():
            if cap:
                new_str += char.upper()
            else:
                new_str += char.lower()
            cap = not cap
        else:
            new_str += char
        
    return new_str

print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")

# Remove consecutive duplicates

'''
algo
- loop through elements of list
- 
'''

def unique_sequence(lst):
    new_lst = [lst[0]]

    for i in range(1,len(lst)):
        if lst[i] != lst[i - 1]:
            new_lst.append(lst[i])
    return new_lst

print(unique_sequence([1, 1, 2, 3, 3, 3, 4, 5, 5, 6]))
# [1, 2, 3, 4, 5, 6]

