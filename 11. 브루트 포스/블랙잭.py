n, m = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] > m:
                continue
            else:
                result = max(result, numbers[i] + numbers[j] + numbers[k])
                
            
print(result)

