s = input()


count = 0
numbers = [-1 for i in range(26)]
for i in s:
    if numbers[ord(i) - 97] == -1:
        numbers[ord(i) - 97] = count
    count += 1
    """print("count =", count, "i =", i)"""

print(*numbers, sep = ' ')