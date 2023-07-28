# https://www.acmicpc.net/problem/11444

# 피보나치 수 6

# 피보나치 수를 나눈 나머지를 구하는 문제

# 피보나치 수를 나눈 나머지는 주기를 가지고 있다.

# 피보나치 숫자 사이의 간격
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 ...
#  0 1 1 2 3 5  8 13 21 34 55  89 144 233 ...

# n번째 + n+1번째 = n+2번째



n = int(input())

def fibo(n):
    print('n: ', n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = fibo(n//2)
        if n%2 == 0:
            return (temp*temp)%1000000007
        else:
            return (temp*temp*fibo(n))%1000000007
        
print(fibo(n))
