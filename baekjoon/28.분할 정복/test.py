print("Hello World!")

# 분할정복 예제
# 1. 재귀함수를 이용한 분할정복

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
    
print(power(2, 3))

# 2. 분할정복을 이용한 거듭제곱
def power(x, y):
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            return power(x*x, y//2)
        else:
            return x * power(x*x, y//2)
        
print(power(2, 3))