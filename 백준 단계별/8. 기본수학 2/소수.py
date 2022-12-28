m = int(input())
n = int(input())
numbers = []
for i in range(m, n+1):
    brk = False
    for j in range(2, i):
        if i % j == 0:
            brk = True
            break
    if brk == True:
        continue
    if i != 1:
        numbers.append(i)
total = 0

for x in numbers:
    total += x
if len(numbers) == 0:
    print("-1")
else:
    print(total)
    print(numbers[0])