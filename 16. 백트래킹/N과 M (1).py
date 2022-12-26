from itertools import combinations

A, B = map(int, input().split())
nums = []
for i in range(1, A+1):
    nums.append(i)
nums = combinations(nums, B)
for i in nums:
    print(i)
