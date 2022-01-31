#if-else
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

#Input Format
# A single line containing a positive integer,n.

## Output Format 
#  Print Weird if the number is weird. Otherwise, print Not Weird.

n = int(input('Please add number: ').strip())
if n % 2 == 1: print('Weird')
else:
    if 2 <= n <= 5: print('Not Weird')
    elif n <= 20: print('Weird')
    else: print('Not Weird')


#2.Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b. The second line should contain the result of float division,  a/b.
# No rounding or formatting is necessary.
#Example
#a = 3
#b = 5
#The result of the integer division 3//5 =0.
#The result of the float division is 3/5 =0.6.

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)


#3.Task
#The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i**2.

# n = int(input())
# for i in range(n):    print(i ** 2)


#4.Task


# def check_leap(year):
#     if (year % 4 ==0) and (year % 100 !=0) or (year % 400 ==0):print('Leap year')
#     else: print('Not leap year')

# year = int(input('Add year:'))
# check_leap(year)

# def check_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0: return True
#         else: return True
#     return False

# year = int(input)
# print(check_leap(year))

# def check_leap(year):
#     if year % 4: return False
#     if not year % 100:
#         if not year % 400: return True
#         else: return False
#     return True
# year = int(input())
# print(check_leap(year))

#5.123...5

# n = int(input())
# for i in range(1,n+1): print(i,end ="")


#6.# Task find string
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# string line: a string of space-separated words
# Returns
# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

# sentence = input('Add any sectence:')#first one
# sentence = sentence.split(" ")
# sentence = "-".join(sentence)
# print(sentence)

# def str_method(str): #second one
#     return "-".join(str.split())

# str = input("Add ant sentence: ")
# print(str_method(str))