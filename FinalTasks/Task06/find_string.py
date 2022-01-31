#find string
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# string line: a string of space-separated words
# Returns
# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

sentence = input('Add any sectence:') #first solution
sentence = sentence.split(" ")
sentence = "-".join(sentence)
print(sentence)

def str_method(str): #second solution
    return "-".join(str.split())

str = input("Add ant sentence: ")
print(str_method(str))