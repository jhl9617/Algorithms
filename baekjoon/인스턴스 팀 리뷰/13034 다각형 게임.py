# https://www.acmicpc.net/problem/13034
# 다각형 게임 
def calculate_grundy(heap, grundy_values):
    if heap in grundy_values:
        return grundy_values[heap]
    mex = set()
    for i in range(1, heap + 1):
        # 재귀적으로 그런디 수 계산
        mex.add(calculate_grundy(heap - i, grundy_values))
    grundy = 0
    while grundy in mex:
        grundy += 1
    grundy_values[heap] = grundy
    return grundy

def nim_game(heaps):
    grundy_values = {}
    xor_sum = 0
    for heap in heaps:
        xor_sum ^= calculate_grundy(heap, grundy_values)
    return xor_sum != 0

# 예제 입력
heaps = [3, 4, 5]
# 게임의 승리 여부 출력
print("Current player can win?" , nim_game(heaps))
