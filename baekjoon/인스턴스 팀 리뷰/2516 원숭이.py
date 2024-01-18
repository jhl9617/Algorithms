# https://www.acmicpc.net/problem/2516
# 원숭이


# KOI 동물원에는 N마리의 원숭이가 있고, 이 원숭이들을 수용할 수 있는 두 개의 큰 우리가 있다. 모든 원숭이들은 1부터 N까지의 번호가 매겨져 있다.

# 원숭이들 사이에는 유달리 서로 앙숙관계인 원숭이들이 있어서 같은 우리에 두었을 경우 서로 싸우는 경우가 많다. 두 원숭이 x와 y가 앙숙관계라는 것은 두 원숭이 x, y가 서로 싫어하는 관계임을 의미한다. 또한, 각각의 한 원숭이에 대해 앙숙관계에 있는 원숭이들의 수는 기껏해야 세 마리라고 가정한다. 동물원에서는 원숭이들의 앙숙관계를 조사하여 아래의 두 조건을 만족하도록 원숭이들을 두 개의 우리에 나누어 수용하려고 한다. 

# (조건 1) 각 원숭이에 대해 같은 우리 안에 있으며 앙숙관계인 원숭이는 한 마리 이하이다.

# (조건 2) 비어있는 우리는 없다. (즉, 하나의 우리에 원숭이를 모두 수용 가능한 경우가 있더라도 각각의 우리에는 적어도 한 마리 이상의 원숭이를 수용하여야 한다.)

# 예를 들어, N=5 인 경우에 1번 원숭이는 {2, 3, 4}와 2는 {1, 3, 5}와 앙숙관계이고, 그리고 3은 {1, 2, 4}와 4는 {1, 3, 5}, 그리고 5는 {2, 4}와 앙숙관계라고 하자. 위의 조건을 만족하도록 원숭이들을 두 개의 우리로 나누려면 {1, 3, 5}를 하나의 우리에, 그리고 {2, 4}를 다른 우리에 수용하면 된다.

# 원숭이들의 수와 각 원숭이들의 앙숙관계가 입력으로 주어질 때, 위의 조건을 만족하도록 원숭이들을 두 개의 우리에 나누어 수용하는 프로그램을 작성하시오. 
import sys
N = int(input())
firstPrison = list()
num = list()
for i in range(N):
    firstPrison.append(sys.stdin.readline().rstrip().split(" "))
    num.append(int(firstPrison[i][0]))

    # list의 첫번째 원소는 원숭이의 번호이다.(1~N)
    firstPrison[i][0] = i+1


print(firstPrison)
print(num)

secondPrison = list()
while True:
    # num 리스트의 최댓값
    max_num = max(num)

    print("max_num : ", max_num)
    print("num : ", num)
    print("firstPrison : ", firstPrison)
    print("secondPrison : ", secondPrison)

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
                        print("format(tmp[0])", format(tmp[0]))
                        if format(tmp[0]) in firstPrison[k]:
                            firstPrison[k].remove(format(tmp[0]))

                            num[k] -= 1

                    # num 리스트에서도 제거한다.
                    num.remove(num[i])
        

                    print("옮긴 후 firstPrison : ", firstPrison)
                    print("옮긴 후 secondPrison : ", secondPrison)
                    print("옮긴 후 num : ", num)
                    
                    break


    
    # firstPrison의 max_num이 1개 이하이면 끝낸다.
    if max_num <= 1:
        break

print(firstPrison)
print(secondPrison)
            





