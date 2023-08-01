# https://www.acmicpc.net/problem/11444

# 피보나치 수 6

#  1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

# 아주 큰 피보나치를 빠르게 구하려면 행렬의 거듭제곱을 이용
# F n+2 = (1 1) (F n+1)
# F n+1 = (1 0) (F n  )

# (1 1)^n
# (1 0)
#   =
# (F n+1 F n  )
# (F n   F n-1)


import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값이다(단, n>=1일때)

def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
            
    return Z

def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])