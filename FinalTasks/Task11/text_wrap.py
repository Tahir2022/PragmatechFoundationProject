#Text Wrap

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:
#1 string string: a long string
# 2int max_width: the width to wrap to

# Returns

# string: a single string with newline characters ('\n') where the breaks should be
# Input Format

# The first line contains a string, string .
# The second line contains the width, max_width.


def wrap(string, max_width):
    a=[]
    c=0
    while len(string)>c:
        a.append(string[c:c+max_width])
        c+=max_width
    return "\n".join(a)
    
string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
result = wrap(string, max_width)
print(result)