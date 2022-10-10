def d(n):
    if n <= 10000: 
        print(n)
        d(n + (n // 10 + n % 10))

d(1)