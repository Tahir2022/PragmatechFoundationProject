#loops

#The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i**2.

# Input Format
# The first and only line contains the integer, n.


n = int(input())
if 1 <= n <= 20:
    for i in range(n):  print(i ** 2)
