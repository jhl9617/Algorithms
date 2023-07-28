import sys


	
#정수 입력
N = int(input())
print(N)

#문자열 입력
a,b = input().split()
print(a, b)

#정수 2개 입력
a,b = map(int, input().split())
print(a,b)

#1줄씩 N번 입력받아서 2차원 배열로 만들기
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
print(arr)

# 정수형 입력 (띄어쓰기로 구분)
arr = list(map(int,input().split()))
print(arr)

# 정수형 입력 (N개 입력받을때)
arr = []
for i in range(N):
	arr.append(int(input()))
	

# 문자열 입력(n값이 엔터 개수)
arr = [int(input()) for _ in range(N)]
    