from itertools import permutations
nums = [1, 1, 3, 4, 5, 6]

listt = permutations(nums,r=3)


for i in listt:
    print(i)