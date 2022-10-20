n = int(input())
numbers = list(map(int, input().split()))
primes = []
two = False
for i in numbers:
    if i == 2:
        two = True
    for j in range(2, i):
        if i % j == 0:
            break
        if i - j == 1:
            primes.append(i)
        
if two == True:
    print(len(primes)+1)
else:
    print(len(primes))