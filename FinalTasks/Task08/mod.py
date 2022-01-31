#Power - Mod Power

# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

a,b,m= int(input()), int(input()), int(input())
print((a**b) % m)