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

# Stack Machine Interpretation

'''
problem
- input: string of commands
- ouptut: output of commands
rules:
    - explicit: sequencially move from left to right getting and doing action requested
    - implicit:

Examples / test cases:
Data structure:
Algo:
- Parse out list of commands to be executed 
- init a stack and register
- build helper function to do things requested
- iterate through list of commands, executing each one
'''



def is_integer(sub):
    try:
        int(sub)
        return True
    except:
        return False

def minilang(commands):
    stack = []
    register = 0

    for command in commands.split():
        # print(f'stack is {stack}')
        # print(f'register is {register}')
        # print(f'command = {command}')
        match command:
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register = register // stack.pop()
            case 'REMAINDER':
                register = register % stack.pop()
            case 'POP':
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                register = int(command) 
    return

minilang('5 PUSH 6 ADD')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed because the `program` argument has no `PRINT` commands)

# Word to Digit

'''
problem:
- input: string
- output: string with numbers swapped to ints
Rules:
    - explicit:
    - implicit:
examples / test cases
data structure:
- dict - keys are str, values are ints
algo:
- build dict
- split into words
- for each word if in dict, get value 
- append to a new string
- return new string
'''
import string

',' in string.punctuation

def word_to_digit(message):
    NUMS = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four' : 4,
        'five' : 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    new_words =[]

    for word in message.split():
        clean_word = word
        first_char = ""
        last_char = ""
        
        while (clean_word[0] in string.punctuation) or (clean_word[-1] in string.punctuation):
            if clean_word[0] in string.punctuation:
                first_char = first_char + clean_word[0]
                clean_word = clean_word[1:]

            if clean_word[-1] in string.punctuation:
                last_char = clean_word[-1] + last_char
                clean_word = clean_word[:-1]
        
        new_words.append(first_char + str(NUMS.get(clean_word.lower(), clean_word)) + last_char)

    return " ".join([word for word in new_words])


message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
print(word_to_digit(message))
# Should print True

# Is it prime?
'''
prob: check if number given is prime
    - input: int
    - output: boolean
algo:
    - iterate through range of 2 to number / 2
        - if remainder of number % iteration == 0:
            - return false
    return true
'''
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

# Fibonacci Numbers

'''
- build up from 2
- sum n1 + n2
- store data n2 --> n1 and new sum --> n2
- continue until your number
'''

def fibonacci(number):
    n1 = 1
    n2 = 1
    new_sum = 1

    for _ in range(3, number + 1):
        new_sum = n1 + n2
        n1 = n2
        n2 = new_sum
    
    return new_sum

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# Fibonacci Numbers (recursion)
fibs = [1 , 1]
def fibonacci(number):
    if number <= len(fibs):
        return fibs[number - 1]
    else:
        fibs.append(fibs[-2] + fibs[-1])
    
    return fibonacci(number - 1) + fibonacci(number - 2)
    
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
print(fibs)

# Fib number location by length
'''
return the first fibanocci sequence of that length
'''
def find_fibonacci_index_by_length(num_digits):
    fib_num = 1

    while True:
        val = fibonacci(fib_num)
        if len(str(val)) >= num_digits:
            break
        fib_num += 1
    return fib_num

def fibonacci(number):
    n1 = 1
    n2 = 1
    new_sum = 1

    for _ in range(3, number + 1):
        new_sum = n1 + n2
        n1 = n2
        n2 = new_sum
    
    return new_sum

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)