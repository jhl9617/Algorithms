import sys

#N은 홀수
N =int(sys.stdin.readline())
nums = []
nu = [0]*500000
tot = 0
max = 0
min = 4000

for i in range(N):
    inp = int(sys.stdin.readline())
    if inp > max: max = inp
    if inp < min: min = inp
    tot += inp
    nu[inp+1] += 1
    nums.append(inp)

print(tot//N)
nums.sort()
if len(nums) == 1:
    print(nums[0])
else:
    print(int(nums[N//2]))
