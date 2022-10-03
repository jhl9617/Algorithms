numbers = [int(input()) for _ in range(10)]
for i in range(10):
    numbers[i] = numbers[i] % 42


result = []
for i in range(10):
    if numbers[i] not in result:
        result.append(numbers[i])
print(len(result))