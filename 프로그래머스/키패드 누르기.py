numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]   
hand = "left"
answer = ''
lefthand = 10
righthand = 12
for i in numbers:
    if i == 0:
        i = 11


    if (i == 3 or i == 6 or i == 9):
        
        answer += 'R'
        righthand = i
    elif (i == 1 or i == 4 or i == 7):
        answer += 'L'
        lefthand = i
    else:
        ledis = abs(i - lefthand) // 3 + abs(i - lefthand) % 3
        ridis = abs(i - righthand) // 3 + abs(i - righthand) % 3

        if ledis > ridis:
            answer += 'R'
            righthand = i
        elif ledis < ridis:
            answer += 'L'
            lefthand = i
        else:
            if hand == "right":
                answer += 'R'
                righthand = i
            elif hand == "left":
                answer += 'L'
                lefthand = i








print(answer)



