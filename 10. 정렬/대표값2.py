list1 = []

total = 0
mid = 0

for i in range(5):
    inp = int(input())
    list1.append(inp)
    total += inp

list1.sort()


print(total // len(list1))
print(list1[len(list1) // 2])