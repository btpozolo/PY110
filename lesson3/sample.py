import pdb

a = 2
def test():
    print("Inside the function!")
    global a
    a = 4

print("Before function call")
test()
print("After function call")