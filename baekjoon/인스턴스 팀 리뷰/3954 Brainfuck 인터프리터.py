# https://www.acmicpc.net/problem/3954
# brainf*ck 인터프리터
def brainfuck_interpreter(sm, sc, si, code, input_string):
    memory = [0] * sm  # 메모리 배열 초기화
    pointer = 0  # 포인터 초기 위치
    pc = 0  # 프로그램 카운터
    input_pointer = 0  # 입력 포인터
    bracket_map = {}  # 괄호 매핑
    executed_commands = 0  # 실행된 명령어 수
    loop_check = set()  # 실행된 루프 체크

    # 괄호 짝 찾기
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            if stack:
                opening = stack.pop()
                bracket_map[opening] = i
                bracket_map[i] = opening

    while pc < sc:
        command = code[pc]
        if command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '>':
            pointer = (pointer + 1) % sm
        elif command == '<':
            pointer = (pointer - 1) % sm
        elif command == '.':
            pass
        elif command == ',':
            if input_pointer < si:
                memory[pointer] = ord(input_string[input_pointer])
                input_pointer += 1
            else:
                memory[pointer] = 255
        elif command == '[':
            if memory[pointer] == 0:
                pc = bracket_map[pc]
        elif command == ']':
            if memory[pointer] != 0:
                pc = bracket_map[pc]

        executed_commands += 1
        if command in '[]':
            loop_check.add((pc, memory[pointer]))
            
            if executed_commands > 50000000 and len(loop_check) < executed_commands / 5000000:
                # 무한 루프 감지
                return "Loops " + str(bracket_map[pc]) + " " + str(pc)

        pc += 1

        if executed_commands > 50000000:  # 횟수 제한 초과
            break

    if executed_commands <= 50000000:
        return "Terminates"
    else:
        # 무한 루프 위치
        opening = min(bracket_map.keys())
        closing = bracket_map[opening]
        return "Loops " + str(opening) + " " + str(closing)



t = int(input())
for _ in range(t):
    sm, sc, si = map(int, input().split()) 
    code = input() 
    input_string = input()
    print(brainfuck_interpreter(sm, sc, si, code, input_string))
