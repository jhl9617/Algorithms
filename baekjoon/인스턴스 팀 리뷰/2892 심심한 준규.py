# https://www.acmicpc.net/problem/2892
# 심심한 준규
import sys

# int로 입력받음
i = int(input()) 

values = sys.stdin.readline().split()
dec_values = []

for values in values:
    dec_values.append(int(values, 16))

# 16진수를 10진수로 변환
for i in dec_values:
    # a ~ z 와 0 ~ 9 사이의 값을 xor 연산하면 64 ~ 95 사이의 값이 나옴
    if 64 <= i <= 95:
        print("-", end='')
    else:
        print(".", end='')
print()