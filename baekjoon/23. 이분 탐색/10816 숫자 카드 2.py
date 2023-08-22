# https://www.acmicpc.net/problem/10816
# 10816번

# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# N = int(input())
# num1 = map(int, input().split())
# M = int(input())
# num2 = map(int, input().split())

# dic = {}
# for i in num1:
#     if i in dic:
#         dic[i] += 1 # dic[i] = dic.get(i, 0) + 1
#     else: 
#         dic[i] = 1  # dic[i] = dic.get(i, 0) + 1

# for i in num2:
#     if i in dic:
#         print(dic[i], end=' ')
#     else:
#         print(0, end=' ')
    

# 2. 이분 탐색을 이용한 풀이

# 이분 탐색을 이용하려면, 정렬이 되어있어야 한다.
# 이분 탐색을 이용하면, O(logN)의 시간 복잡도로 탐색이 가능하다.

# 이분 탐색을 이용한 풀이는 다음과 같다.

# 1. 상근이가 가지고 있는 숫자 카드를 정렬한다.

# 2. 이분 탐색을 이용하여 상근이가 가지고 있는 숫자 카드 중에서, 이분 탐색으로 찾으려는 숫자가 처음 등장하는 위치와 마지막으로 등장하는 위치를 찾는다.

# 3. 마지막으로 등장하는 위치에서 처음 등장하는 위치를 빼주면, 상근이가 가지고 있는 숫자 카드 중에서 이분 탐색으로 찾으려는 숫자가 몇 개 있는지 알 수 있다.

# 4. 이분 탐색으로 찾으려는 숫자가 상근이가 가지고 있는 숫자 카드에 없다면, 처음 등장하는 위치와 마지막으로 등장하는 위치를 찾았을 때, 두 값이 같다. 이때는 상근이가 가지고 있는 숫자 카드 중에서 이분 탐색으로 찾으려는 숫자가 없다는 것을 알 수 있다.

# 5. 이분 탐색으로 찾으려는 숫자가 상근이가 가지고 있는 숫자 카드에 있다면, 처음 등장하는 위치와 마지막으로 등장하는 위치를 찾았을 때, 두 값이 다르다. 이때는 상근이가 가지고 있는 숫자 카드 중에서 이분 탐색으로 찾으려는 숫자가 있다는 것을 알 수 있다.

# 이분탐색 풀이

import sys
from collections import Counter
# N은 int로 받아야 한다.
N = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

num1 = sorted(num1)

num1_counter = Counter(num1)  # 중복된 값의 개수를 미리 계산하여 저장 Counter({10: 3, -10: 2, 3: 2, 2: 1, 6: 1, 7: 1})


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:

            # count 시간복잡도 N
            return num1_counter[target]
        elif array[mid] > target: # 중간값보다 작으면 왼쪽 확인
            end = mid - 1
        else: # 중간값보다 크면 오른쪽 확인
            start = mid + 1
    
    return 0

for i in num2:
    result = binary_search(num1, i, 0, N-1)
    print(result, end=' ')

