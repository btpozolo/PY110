# 1 
'''
 problem: return the number of numbers smaller than the item in a new list
    - input: list of ints
    - output: list of ints 
    Rules:
    - explicit: if there duplicate numbers below only count them once
    - implicit: empty lists? Do we modify in place?
data structure:
- iterate through each element of the list
    - count the amount of elements in this list that are less than current item
        - deduped (maybe use a set)
    - append answer to new list
- return new list
 '''
def smaller_numbers_than_current(lst_ints):
    unique_ints = list(set(lst_ints))

    new_list = [len([1 for element in unique_ints if element < item])
        for item in lst_ints
    ]
    
    return new_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# 2 

'''
problem: return minimum sum of 5 consective integers in list
input: list of integers
ouput: int (sum of 5 consecutive integers) if under 5, return none
data structure:
- range and one total
algo:
- check if list has 5 elements, if not return none
- initialize current sum to first 5 numbers
- iterate through each subsequent for each set of 5 numbers
    - calculate the sum
    - if sum greater than current sum, set to current sum
- return current sum
'''
def minimum_sum(int_list):
    if len(int_list) < 5:
        return None
    
    list_5s = [sum(int_list[ idx : idx + 5])
               for idx in range(0, len(int_list) - 4)]
    print(f'{list_5s = }')
    return min(list_5s)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

'''
prob: function takes a string and returns a copy with every second character in every third word converted to uppercase
input: string
ouptut: string
algo:
- init a list of strings for new words
- iterate through word
    - if word is third iterate through char
         - init a new word
         - if char % 2 == 0, concat uppercase, else concat letter

'''
def upper_word(word):
    chars = [ char.upper() if (idx + 1) % 2 == 0 else char
        for idx, char in enumerate(word)
    ]
    return "".join(chars)

print(upper_word('hello'))

def to_weird_case(sentence):
    new_list = [upper_word(word) if (idx + 1) % 3 == 0 else word
        for idx, word in enumerate(sentence.split())
    ]
    return " ".join(new_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

'''
prob: func that gets tuple of 2 numbers closest together in value. If multiple pairs return pair that occurs first
- input : list of ints
- output: tuple of 2 numbers closest together in value
rules:
    - explicit: if same return closest pair (by max index, min, combined?)
    - implicit: do we need to handle empty list of less than 2 elements?
data structure:
- list
algo:
- init closest_distance = 2nd and 1st element in sorted list
- init closest_nums = (1st and 2nd elements)
- iterate through 2nd to last element in list
    - iterate through each elements as starting element
    - get the abs difference between that and prior element
        - if less than:
            - replace closest_nums and closest_distance
    

- return closest_nums
'''
def closest_numbers(numbers):
    closest_distance = abs(numbers[0] - numbers[1])
    closest_nums = [(numbers[0], numbers[1])]

    for start_idx, first_num in enumerate(numbers):
        print(f'{start_idx = } {first_num = }')
        for second_num in numbers[start_idx + 1: ]:
            print(f'{second_num = }')
            curr_diff = abs(first_num - second_num)
            if curr_diff < closest_distance:
                closest_distance = curr_diff
                closest_nums = [(first_num, second_num)]
            elif curr_diff == closest_distance:
                closest_nums.append((first_num, second_num))
            

    print(f'{closest_distance = } \n{closest_nums = }')
    
    last_digit = [numbers.index(pair[1])
        for pair in closest_nums
    ]

    idx = last_digit.index(min(last_digit))

    # last_digit = [ max(numbers.index(n1), numbers.index(n2))
    #     for pair in closest_nums
    #     for n1, n2 in pair
    # ]
    print(f'{last_digit = }')
    print(f'{idx = }')
    return closest_nums[idx]

print(closest_numbers([1, 10, 14, 5]) == (10, 14))

closest_numbers([1 ,22, 24, 5,43,412])

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))


# 5

'''
problem: return char of greatest freq  
input - string
output - char 
rule:
- upper and lower case should be the same
- if tie return one that is first

algo:
- lowercase whole string
- create dict of each letter and frequency
- f
'''

def most_common_char(sentence):
    s = sentence.lower()

    char_freq = {char : s.count(char) 
        for char in set(s)
    }
    max_freq = max(char_freq.values())

    max_items = [ 
        (s.find(char), char)
        for char, freq in char_freq.items()
        if freq == max_freq
    ]
    max_items.sort()

    return max_items[0][1]

print(most_common_char('Hello World'))

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

'''
prob: create func that returns a dict object with keys as lowercase letters and values 
inputs: string
output: dict of char, count pairs

algo:
- get set of unique lower case letters
- iterate through set of unique letters adding letter and count to a dict

'''
def count_letters(string):
    unique_letters = set([char for char in string if char.isalpha() and char.islower()])

    letter_freq = {letter: string.lower().count(letter) for letter in unique_letters }
    print(f'{letter_freq = }')
    return letter_freq


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('Wowebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})


'''
prob: return number of identical pairs 
    - input: list of ints
    - ouptup: int - number of identical pairs of ints in the list
algo:
- initialize a new list of ints
- init an int complete_pairs
- iterate through each element in given list
    - check if in new list
        - if so, remove from new list and increment complete_pairs
        - if not, append to new list
- return complete_pairs
'''
def pairs(list_of_ints):
    helper_list = []
    complete_pairs = 0

    for number in list_of_ints:
        if number in helper_list:
            helper_list.remove(number)
            complete_pairs += 1
        else:
            helper_list.append(number)

    return complete_pairs



print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

'''
prob: get longest vowel substring of string
    - input: string - lowercase letters
    - output: int of longest vowel substring
algo:
- init vowel_sub = 0
- init curr_sub = 0
- iterate through char of string:
    - check if vowel:
        - if so, increment curr_sub
            - set vowel_sub = max (vowel_sub, curr_sub)
        - if not, curr_sub = 0
'''

def longest_vowel_substring(string):
    vowel_sub, curr_sub = 0, 0
    VOWELS = 'aeiou'
    for char in string:
        if char in VOWELS:
            curr_sub += 1
            vowel_sub = max(curr_sub, vowel_sub)
        else:
            curr_sub = 0
    return vowel_sub

def longest_vowel_substring(string):
    string.split()

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)


'''
prob:
    - input: two strings
    - output: int - number of times 2nd string occurs in the first
-rules:
    - overlapping does not count
-algo:
    - using count method 
    while find not -1, 
        - 
        - find substring in string
'''
def count_substrings(s1, s2):
    return s1.count(s2)

def count_substrings(s1, s2):
    num_occurances = 0
    while True:
        if s1.find(s2) < 0:
            break
        num_occurances += 1
        s1 = s1[s1.find(s2) + len(s2):]
    return num_occurances
    


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

'''
prob: 
    - inputs: string of digits
    - outputs: int - num of even numbered substrings that can be formed
- rules:
    - multiple occurances of same substring can count mult times
-algo:
- create list of all possible substrings
    - start with first char:
        - iterate through all possible endings
    - iterate through each starting char
- check if each is even
- return number of even ones
'''
def get_all_substrings(string):
    subs = []
    n = len(string)

    for i in range(n):
        for j in range(i + 1, n + 1):
            subs.append(string[i:j])
    return subs


print(get_all_substrings('12355'))

def even_substrings(number):
    substrings = get_all_substrings(number)
    even_subs = 0

    for substring in substrings:
        if int(substring) % 2 == 0:
            even_subs += 1
        
    return even_subs

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

'''
problem: return tuple with string and integer that is the shortest possible substring, s.t. s == t * k
    - input: string
    - output: tuple (string, integer - num of times to repeat it)

data structure:
    - 
algo:
    - get length of string
    - start with first char - see if whole string is that, 
    - continue incrementing length of string checked, until its full string
'''

def repeated_substring(string):
    n = len(string)
    for i in range(1, n // 2 + 1):
        num_times = n // len(string[:i])
        if string[:i] * num_times == string:
            return(string[:i], num_times)
    
    return (string, 1)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

'''
problem: check if string is a panagram (contains every letter in alphabet)
    - input: string
    - output: boolean

- algo:
    - create a dict for each alphabetic letter and its frequency in string
    - if the len of that dict = 26, True, else false
'''

def is_pangram(string):
    unique_chars = set(string.lower())
    freq_dict = [{char: string.count(char) } for char in unique_chars 
                 if char.isalpha()]
    return len(freq_dict) == 26

print(is_pangram('hello'))

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

'''
prob: check if 2nd string can be made from first
    - input: two strings
    - output: Boolean, if some portion of characters in first string can be rearranged to match 2nd
data struct:
    - dict - count chars
algo:
    - create a dict that is each char of first with count of amount
    - iterate through 2nd string 
        - decrease count by 1
        - if less than 0 return false
    - return true
    '''

def unscramble(s1, s2):

    char_freq = {char: s1.count(char)
        for char in set(s1)
    }

    for char in s2:
        char_freq[char] = char_freq.get(char, 0) - 1
        if char_freq[char] < 0:
            return False
        
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

'''
prob: takes an int and returns the sumr of all multiples of 7 or 11 that are less than argument. 
if multiple of both count only once
    - input: int
    - output: int
algo:
    - create a list of all numbers multiple of 7 
    - create a list of all numbers multiple of 9 and not multiple of 7 
        - or do an intersection of two lists
    - sum the lists
    - return the sum
'''

def seven_eleven(number):
    mults_7 = list(range(7, number, 7))
    mults_11 = list(range(11, number, 11))

    mult_7_or_11 = set(mults_7).union(set(mults_11))
    return sum(mult_7_or_11)

def seven_eleven(number):
    mult_7 = [num
        for num in range(number)
        if num % 7 == 0
    ]
    mult_11 = [num
        for num in range(number)
        if num % 11 == 0 
        if num % 7 != 0
    ]
    return sum(mult_7) + sum(mult_11)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)


'''
algo:
-  create list of each 4 digit product
- return max of list
'''

def greatest_product(number):
    ints = [int(digit) for digit in number]
    print(f'{ints = }')
    products = [ ints[idx - 3] * ints[idx - 2] * ints[idx - 1] * ints[idx] 
        for idx in range(3,len(ints))
    ]

    print(f'{products = }')
    return max(products)

def greatest_product(number):
    curr_greatest = 0
    for idx in range(4, len(number) + 1):
        curr_nums = number[idx - 4: idx ]
        curr_nums = [int(digit) for digit in curr_nums]
        print(f'{curr_nums = }')
        curr_prod = 1
        for item in curr_nums:
            curr_prod *= item
        print(f'{curr_prod = }')
        if curr_prod > curr_greatest:
            curr_greatest = curr_prod
    
    return curr_greatest

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

'''
algo:
    - dict of letters and frequency
    - list of frequency if > 1
    - return length of that list
'''

def distinct_multiples(string):
    char_freq = dict()
    
    for char in string:
        char = char.casefold()
        char_freq[char] = char_freq.get(char, 0) + 1
    
    over_2_freq = [ value
        for value in char_freq.values()
        if value >= 2
    ]
    return len(over_2_freq)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

'''
prob: return int to make the sum of the list the next greatest prime number
    - input: list of ints
    - output: int to add to make sum prime
algo:
    - find next highest prime number?
        - check each int from 2 --> number // 2 to see if there is a remainder
        - if so break and check next int
        - if not, save this value and break loop
    - next highest prime value - sum of current int list 
    - return this
'''

def nearest_prime_sum(int_list):
    sum_list = sum(int_list)

    next_prime = 0
    curr_guess = sum_list + 1

    while True:
        for num in range(2, curr_guess):
            if curr_guess % num == 0:
                curr_guess += 1
                continue
            if num == curr_guess - 1:
                next_prime = curr_guess
                return next_prime - sum_list
        
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37
# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

'''
prob: return index where left and right sides are balanced for a sum, if not possible return -1
    - input: list of ints
    - output: int - index where sums are balanced
rules:
    - if multiple spots return the lowest
algo:
    - iterate through indexes in list:
        - check if left and right are equal
            - if so return index
    - return -1
'''

def equal_sum_index(int_list):
    for idx in range(len(int_list)):
        left_side = sum(int_list[:idx])
        right_side = sum(int_list[idx + 1:])
        if left_side == right_side:
            return idx
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

'''
prob: return integer that appears odd number of times, there will only be 1
    - input: list of ints
    - output: integer that appears an odd number of times
algo:
    - init new list
    - iterate through ints in list
        - if int not in new list, append
        - if int in new list, remove
    - return new list element 0
'''

def odd_fellow(int_list):
    freq = []

    for num in int_list:
        if num in freq:
            freq.remove(num)
        else:
            freq.append(num)
    
    return freq[0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

def what_is_different(int_list):
    freq_dict = {num : int_list.count(num) for num in set(int_list)}
    
    for key, value in freq_dict.items():
        if value == 1:
            return key

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

