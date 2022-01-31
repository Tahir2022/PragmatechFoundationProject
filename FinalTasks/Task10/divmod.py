#Mod Divmod

# One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder .

# For example:

# >>> print divmod(177,10)
# (17, 7)
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).

##Input Format
# The first line contains the first integer, a, and the second line contains the second integer, b.

a,b=int(input()), int(input())
print((a//b, a%b))