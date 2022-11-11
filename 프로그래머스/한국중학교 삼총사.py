from itertools import combinations

answer = 0
number = [-1, 1, -1, 1]
num = combinations(number,3)
for i in num:
    if i[0] + i[1] + i[2] == 0:
        print(i[0],i[1],i[2])
        answer += 1


        