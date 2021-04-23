# Write a Python program to find maximum and the minimum value in a set
set1 = set()
n = int(input())

for i in range(n):
    set1.add(i)
print(max(set1))
print(min(set1))