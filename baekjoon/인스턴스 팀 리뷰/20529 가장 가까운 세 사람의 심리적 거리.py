# https://www.acmicpc.net/problem/20529
# 가장 가까운 세 사람의 심리적 거리

# n개 보다 많은 물건을 n개의 집합에 나누어 넣는다면 적어도 어느 한 집합에는 2개 이상의 물건이 속하게 된다는 내용이 비둘기집의 원리

from itertools import combinations

# 두 학생의 심리적 거리
def distance(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        # ('I', 'E'),('n', 's'),('f', 'f'),('p', 'j') 이런식으로 pair로 됨 
        if c1 != c2:
            count += 1
    return count


def mbti_calc(students):
    # 비둘기집의 원리
    # 학생이 33명 이상이면 같은 mbti를 가진 학생이 3명 이상이므로 0
    if len(students) > 32:
        return 0


    result = float('inf')
    for comb in combinations(students, 3):
        # students에서 3개짜리 조합을 만들어 줌
        dist = 0
        for i in range(3):
            for j in range(i+1, 3):
                dist += distance(comb[i], comb[j])
        result = min(result, dist)
    return result

# ------------------------시작----------------------------
T = int(input())
for _ in range(T):
    N = int(input())
    students = list(input().split())
    if N < 3:
        print(0)
    else:
        print(mbti_calc(students))