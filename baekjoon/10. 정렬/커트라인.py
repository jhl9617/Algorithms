N, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
print(numbers[K-1])