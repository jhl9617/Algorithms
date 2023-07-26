# 이항계수 :주어진 크기 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수

# 이항계수의 계산
# 1. nCk = n! / (k! * (n-k)!)

# 이항계수의 성질
# 1. nCk = nCn-k
# 1.1 nC0 = nCn = 1

# 2. nCk = n-1Ck-1 + n-1Ck
# 3. nCk = n-1Ck-1 * n/k

# nC0 = nCn = 1
# 전체 집합에서 아무것도 고르지 않는 방법은 1가지이고, 동시에 모두를 선택하는 것도 1가지 방법뿐이다.

# nCk = n-1Ck-1 + n-1Ck
# 이항계수를 그보다 작은 2개의 부분식으로 나누어 표현할 수 있다.

# def bino_coef(n, k):
#     if k == 0 or n == k:
#         return 1
#     return bino_coef(n-1, k) + bino_coef(n-1, k-1)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

# 팩토리얼 값 계산(나머지 연산 적용)
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

top = factorial(N)
bot = factorial(N-K) * factorial(K) % p


 

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(top * square(bot, p-2) % p)
    








# DP코드.

def bino_coef_dp(n, k):
    cache = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    def bino_coef(n, k):
        if k == 0 or n == k:
            return 1
        if cache[n][k] != -1:
            return cache[n][k]
        cache[n][k] = bino_coef(n-1, k) + bino_coef(n-1, k-1)
        return cache[n][k]
    return bino_coef(n, k)

# 이 함수는 O(nk)의 시간복잡도를 가진다.

# nCk = n-1Ck-1 * n/k

def bino_coef_dp2(n, k):
    cache = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    def bino_coef(n, k):
        if k == 0 or n == k:
            return 1
        if cache[n][k] != -1:
            return cache[n][k]
        cache[n][k] = bino_coef(n-1, k-1) * n/k
        return cache[n][k]
    return bino_coef(n, k)


