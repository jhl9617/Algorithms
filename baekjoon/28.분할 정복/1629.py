import sys

#거듭제곱
#자연수 A를 B번 곱한 수를 알고 싶다.  a, b, c는 2,147,483,647보다 작거나 같은 자연수이고 c로 나눈 나머지를 출력한다.

# 나머지 분배 법칙
# (AxB)%C = (A%C) *(B%C) % C

# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
# ...
a,b,c = map(int,sys.stdin.readline().split())

def power(a,b):
    if b == 1:
        return a%c
    else:
        temp = power(a,b//2)
        if b%2 == 0:
            return (temp*temp)%c
        else:
            return (temp*temp*a)%c
        
print(power(a,b))


