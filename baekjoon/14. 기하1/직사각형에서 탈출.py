x, y, w, h = map(int, input().split())

numbers = []

numbers.append(w-x)
numbers.append(x)
numbers.append(h-y)
numbers.append(y)

print(min(numbers))