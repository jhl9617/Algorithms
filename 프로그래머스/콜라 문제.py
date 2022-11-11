"""132267"""

a, b, n = 3, 2, 20
answer = 0

while n >= a:
    etc = n % a
    print("n, answer: ",n, answer)
    answer += (n // a) * b
    print(n // a * b," 추가")
    n = n // a * b
    n += etc
    
print(answer)