#1 
# count the number of occurances of 'banana'

fruits = ("apple", "banana", "cherry", "date", "banana")
fruits.count('banana')

#3
# create a set that is unique values from both

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a | b)

#4 

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions) # dict{"Fred": 0, "Barney": 1, "Wilma" : 2, ....} note doesn't output 'dict'

#5

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(sum(ages.values()))

#6
print(min(ages.values()))

#7
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

#8

statement = "The Flintstones Rock"

freq_dict = {}
clean_statement = statement.replace(" ", "")

for char in clean_statement:
    freq_dict[char] = freq_dict.get(char, 0) + 1

print(freq_dict)

#9 
[num for num in [1, 2, 3] if num > 1] 

#10
