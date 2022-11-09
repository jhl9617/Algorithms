"""ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
rang = len(ingredient) - 3
count = 0
answer = 0
print(ingredient)
while count < rang:
    if len(ingredient) < 3:
        break

    print(count)
    if ingredient[count] == 1:
        if ingredient[count+1] == 2:
            if ingredient[count+2] == 3:
                if ingredient[count+3] == 1:
                    answer += 1
                    del ingredient[count:count+4]
                    print("남은배열=",ingredient)
                    count = 0
                    continue
    count += 1
print("answer=",answer)
 """
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
answer = 0
stack = []

for burger in ingredient:
    stack.append(burger)
    if len(stack) >= 4:
        print(stack)
        if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1



print(answer)


        
        