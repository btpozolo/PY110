# Lettercase Percentage

'''
problem:
- input: string
- output: dict of 3 properties, % lower, % upper, % neither
rules:
- explicit:
    - at least 1 number
data structure:
- dict
algo:
- iterate through each char of string
- check if alphabetic 
- if so check if its lower or upper
- increment a count
- return counts cleaned up
'''
def letter_percentages(word):

    lowers = 0
    uppers = 0
    neither = 0

    for char in word:
        if char.isalpha():
            if char.islower():
                lowers += 1
            else:
                uppers += 1
        else:
            neither += 1
    
    lowers /= len(word) 
    uppers /= len(word)
    neither /= len(word)

    perc = {
        'lowercase':    f"{lowers * 100:.2f}%",
        'uppercase':    f"{uppers * 100:.2f}%",
        'niether':      f"{neither * 100:.2f}%",
    }

    return perc


print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }

# Triangle sides

'''
input: 3 ints 
output: string of type of triangle or invalid
algo:
- check if valid (all sides > 0 ), sum of two smaller sides > longer side
- if valid check if all sides are same
- check if all sides are different
- return triangle type

'''
sorted_sides = [1, -2, 3]
all([side > 0 for side in sorted_sides])

def triangle(s1, s2, s3):
    short, mid, long = sorted((s1, s2, s3))
    print(short, mid, long)
    sorted_sides = sorted([s1, s2, s3])
    type = ""

    def is_valid(sorted_sides):
        return (
                
                all([side > 0 for side in sorted_sides]) and 
                sum(sorted_sides[:-1]) > sorted_sides[-1]
                )
    
    if not is_valid(sorted_sides):
        type = 'invalid'
    elif all([side == sorted_sides[1] for side in sorted_sides]):
        type = 'equilateral'
    elif len(set(sorted_sides)) == len(sorted_sides):
        type = 'scalene'
    else:
        type = 'isosceles'

    return type

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(5, 4, 3) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# Tri-angles

'''
input: 3 angles ints
outupt: string of type of triangle 
rules:
    - valid - sum = 180 AND all > 0
data structure:
- 
algo:
- check if valid
- return type of triangle
'''

def is_valid(angles):
    return (sum(angles) == 180 and min(angles) > 0)

def triangle(s1, s2, s3):
    sorted_sides = sorted([s1, s2, s3])

    if not is_valid(sorted_sides):
        return 'invalid'
    elif sorted_sides.count(90) == 1:
        return 'right'
    elif max(sorted_sides) > 90:
        return 'obtuse'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Unlucky Days

'''
input: year
output: int number of friday 13ths 
rules:
- explicit:
    - assume year is over 1752
    - modern gregorian calander
- implicit: 
    - return between 0 --> 12

data structure:
- for loop of months
- int for # of fri 13ths
algo:
- for each month
- check if 13th day weekday = Friday
- if so increment counter
- return total
'''
import datetime as dt

def friday_the_13ths(year):
    counter = 0
    for month in range(1, 13):
        if dt.date(year, month, 13).isoweekday() == 5:
            counter += 1
    return counter

friday_the_13ths(1986)      # 1
friday_the_13ths(2015)      # 3
friday_the_13ths(2017)      # 2

# Next Featured Number

'''
problem: featured number is odd, multiple of 7, and all of the digits appear just once
input: int
output: int - next featured number
rules:
- explicit:
    - error handle for if over 9876543201
data structure:
- 
algo:
- start at the closest multiple of 7:
- while conditions aren't met increase by 7 
'''
def is_odd(num):
    return num % 2 != 0

def is_digits_once(num):
    return len(set(str(num))) == len(str(num))

def featured(number):
    if number > 9876543200:
        return 'There is no possible number that fulfills those requirements.'
    
    current_guess = ((number // 7) * 7) + 7

    while True:
        if is_odd(current_guess) and is_digits_once(current_guess):
            return current_guess
        current_guess += 7
    return


print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."

# Sum square - square sum

'''
desc: return difference between (all numbers including current summed) ** 2 and sum (each number ** 2)
input: int
output: int
algo:
- build range (1, number + 1)
- sum(list comprehension [num ] ** 2 for num in range)
'''
def sum_square_difference(number):
    nums = list(range(1, number + 1))
    sum_square = sum(nums) ** 2
    square_sum = sum([num ** 2 for num in nums])
    return sum_square - square_sum


print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150

# Bubble Sort
def bubble_sort(lst):
    
    while True:
        counter = 0
        for index in range(1, len(lst)):
            if lst[index] < lst[index - 1]:
                store = lst[index - 1]
                lst[index - 1] = lst[index]
                lst[index] = store
        
                counter += 1
        if counter == 0:
            break
    return lst




lst1 = [5, 3]
bubble_sort(lst1)
print(lst1)    # [3, 5]

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)    # [1, 2, 4, 6, 7]

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
bubble_sort(lst3)
print(lst3)    # ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
