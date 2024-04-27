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