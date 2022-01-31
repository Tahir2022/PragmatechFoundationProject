#what is your name?

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
# Input Format
# The first line contains the first name, and the second line contains the last name.
# Constraints
# The length of the first and last names are each ≤ 10.

def greetings(first, last):
    if (len(first_name) <= 10) and (len(last_name) <= 10):
        print(f'Hello {first_name} {last_name}! You just delved into python.')
    

first_name = input('Add your first name: ')
last_name = input('Add your last name: ')
greetings(first_name,last_name)


