t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    numbers =[1]*(n + 1)
    for i in range(k + 1):
        for j in range(n):
            
            numbers[j+1] = numbers[j] + numbers[j+1]
            
    
    print(numbers[n-1])