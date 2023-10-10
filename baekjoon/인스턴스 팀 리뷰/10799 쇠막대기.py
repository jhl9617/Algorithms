# https://inuplace.tistory.com/844
# 쇠막대기


def solution():
    s = input()
    stack = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            stack.pop()

            #  () 모양일때(레이저 발사) '(' 갯수만큼 cnt 증가
            if s[i-1] == '(':
                cnt += len(stack)
            # 남은 '('를 하나 없애면서 cnt 1 증가
            else:
                cnt += 1
        
        
    
    return cnt

# ------------------------시작----------------------------
print(solution())


# 과정
# ()(((()())(())()))(())
# count:  0 :  ['(']
# count:  0 :  []
# count:  0 :  ['(']
# count:  0 :  ['(', '(']
# count:  0 :  ['(', '(', '(']
# count:  0 :  ['(', '(', '(', '(']
# count:  3 :  ['(', '(', '(']
# count:  3 :  ['(', '(', '(', '(']
# count:  6 :  ['(', '(', '(']
# count:  7 :  ['(', '(']
# count:  7 :  ['(', '(', '(']
# count:  7 :  ['(', '(', '(', '(']
# count:  10 :  ['(', '(', '(']
# count:  11 :  ['(', '(']
# count:  11 :  ['(', '(', '(']
# count:  13 :  ['(', '(']
# count:  14 :  ['(']
# count:  15 :  []
# count:  15 :  ['(']
# count:  15 :  ['(', '(']
# count:  16 :  ['(']
# count:  17 :  []