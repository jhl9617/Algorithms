# https://www.acmicpc.net/problem/2733
# brainf*ck

ptr = 0
arr = [0] * 32768
code = ''
res = []
index_map = dict()

def parse(idx):
    global ptr, arr, code, index_map
    ch = code[idx]

    if ch == '>':
        if ptr == 32767:
            ptr = 0 
        else:
            ptr += 1
    elif ch == '<':
        if ptr == 0:
            ptr = 32767 
        else:
            ptr -= 1
    elif ch == '+':
        if arr[ptr] == 255:
            arr[ptr] = 0 
        else:
            arr[ptr] += 1
    elif ch == '-':
        if arr[ptr] == 0:
            arr[ptr] = 255
        else:
            arr[ptr] -= 1
    elif ch == '.':
        res.append(chr(arr[ptr]))
    elif ch == '[':
        if arr[ptr] == 0:
            return index_map[idx] + 1 
    elif ch == ']':
        if arr[ptr] != 0:
            return index_map[idx]
    return idx + 1

# ----------시작-------------
n = int(input())
for i in range(1, n + 1):

    # 초기화
    ptr = 0
    index_map.clear()
    arr = [0] * 32768

    res.append("PROGRAM #%d:\n" % i)
    buf = []
    while True:
        line = input().replace(" ", "")
        if 'end' == line:
            break

        # %가 나오기 전까지만 코드로 인식해서 저장
        buf.append(line[:line.find('%')] if '%' in line else line)
    code = ''.join(buf)

    # '['와 ']' 의 위치를 매핑
    stk = []
    
    error = False
    for j in range(0, len(code)):
        ch = code[j]
        if ch == '[':
            # 스택에 현재 인덱스 저장
            stk.append(j)
        elif ch == ']':
            # '[' 가 스택에 없는데 ']'가 나오면 에러 발생시킴
            if len(stk) == 0:
                error = True
                break
            # 스택에서 pop하면서 현재 인덱스와 스택에서 pop한 인덱스를 매핑
            idx = stk.pop()
            index_map[j] = idx
            index_map[idx] = j

    if len(stk) == 0 and not error:
        k = 0
        while k < len(code):
            k = parse(k)
    else:
        res.append('COMPILE ERROR')
    res.append('\n')
print(''.join(res))


