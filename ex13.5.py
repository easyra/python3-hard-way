from sys import argv

script, first, second = argv
print(first + second)
name = input('Name: ')

print(f"{name} says: '{first + second}'")