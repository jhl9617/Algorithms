n = int(input())
numbers = list(map(int, input().split()))
M = int(max(numbers))
for i in range(n):
    numbers[i] = numbers[i] / M * 100
    
result = sum(numbers)
print(result / n)
     

