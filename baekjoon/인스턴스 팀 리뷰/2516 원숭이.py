# https://www.acmicpc.net/problem/2516

# https://cooing-food-943.notion.site/2516-5577dcb026db4fe19e7747c68f354568?pvs=4
# 문제 해결 아이디어

import sys
N = int(input())
firstPrison = list()
num = list()
for i in range(N):
    firstPrison.append(sys.stdin.readline().rstrip().split(" "))
    num.append(int(firstPrison[i][0]))

    # list의 첫번째 원소는 원숭이의 번호이다.(1~N)
    firstPrison[i][0] = i+1

secondPrison = list()
while True:
    # num 리스트의 최댓값
    max_num = max(num)

    # firstPrison 의 list 갯수만큼 for문을 돌면서 가장 많은 앙숙을 가진 원숭이를 찾는다.

    for i in range(len(firstPrison)):
        # 가장 많은 앙숙을 가진 원숭이를 찾았을때
        # firstPrison[i]의 원소 갯수 - 1 이 max_num와 같을 때 
        if num[i] == max_num:
            print("num[i] : ", num[i] , ", max_num : ", max_num)
            # secondPrison로 이동했을때 그 원숭이의 앙숙이 2개 이상이 되는지 확인
            # secondPrison이 [[1, '2', '3', '4'], [3, '1', '2', '4']] 일때 
            # 넘기려는 4번 원숭이가 [4, '1', '3', '5'] 이면 앙숙이 1, 3번 원숭이 즉 2개 이상이므로 넘어갈수 없다
            # 넘기려는 원숭이가 [5, '2', '4'] 이면 앙숙이 1개 이하이므로 넘어간다.

            # 넘어갔을때 secondPrison에 앙숙이 2개 이상이면 넘어갈수 없다.
                # firstPrison[i]의 원소들로 for문을 돌면서 secondPrison의 원소들중에 2개 이상이면 넘어갈수 없다.
            for j in range(1, num[i]):
                count = 0
                for k in range(1,len(secondPrison)):
                    if firstPrison[i][j] in secondPrison[k]:
                        count += 1
                if count >= 2:
                    break
                # secondPrison에 앙숙이 1개 이하이면 넘어간다.
                else:
                    # 넘어가기 전에 원숭이 번호 i를 가진 firstPrison의 원숭이 리스트에서 'i' 를 모두 제거한다.
                    # 그리고 secondPrison에 넘긴다.
                    # 그리고 num 리스트에서도 제거한다.

                    tmp = firstPrison[i]
                    secondPrison.append(firstPrison[i])
                    firstPrison.remove(firstPrison[i])
                    
                    # for문을 돌며 tmp의 번호가 firstPrison의 원소 중에 있는지 확인해서 있으면 제거한다.
                    # 그 이후 num을 -1 해준다.
                    for k in range(len(firstPrison)):
                        
                        if format(tmp[0]) in firstPrison[k]:
                            firstPrison[k].remove(format(tmp[0]))
                            num[k] -= 1

                    # num 리스트에서도 제거한다.
                    num.remove(num[i])

                    break

    # firstPrison의 max_num이 1개 이하이면 끝낸다.
    if max_num <= 1:
        break

print(len(firstPrison), firstPrison, sep=" ")
print(len(secondPrison), secondPrison, sep=" ")