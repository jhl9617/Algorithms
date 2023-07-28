# https://www.acmicpc.net/problem/28117
# prlong longf

import sys

# 문자열 4개 long인지 확인
def longDecider (i):
    return a[i:i+4] == 'long'


N = int(input())
a = list(sys.stdin.readline().rstrip())

answer = 0

# 문자열을 리스트로 변환
i = 0
while i < N:
    print('i = ', i," ||| ", a[i])
    tmp = 0
    if a[i] == 'l'and N - i - 4 > 3:
        print('1번째 long 자리 있는지 N - i - 4 = ', N - i - 4)
        print(a[i:i+4])
        if longDecider(i):
            print('첫번째 long')
            i += 4
            tmp += 1


            if N - i - 8 > 3:
                print('2번째 long 자리 있는지 N - i - 8 = ', N - i - 8)
                if longDecider(i):
                    i += 4
                    print('두번째 long')
                    tmp += 1

                    if N - i - 12 > 3:
                        i += 4
                        print('3번째 long 자리 있는지 N - i - 12 = ', N - i - 12)
                        if longDecider(i):
                            print('세번째 long')
                            tmp += 1

    i += 1

        
print (answer)



            
            
           