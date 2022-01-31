# Symmetric difference

# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer,M .
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

x=input()
a=list(map(int, input().split()))
a=set(a)
y=input()
b=list(map(int, input().split()))
b=set(b)
d=list(a.difference(b))+list(b.difference(a))
d.sort()
for x in d:
    print(x)