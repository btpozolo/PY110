a = "".join(sorted('fdsafhlkjfdsfdsafds'))
print(a)

animals = ["Cat", "dog", "ZEBRA", "monkey"]
sorted_animals = sorted(animals, key=str.lower)
print(sorted_animals)     # ["Cat", "dog", "monkey", "ZEBRA"]