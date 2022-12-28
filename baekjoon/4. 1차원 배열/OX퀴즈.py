n = int(input())

for _ in range(n):
    quizz = list(input())
    conseq = 0 
    score = 0
    for ox in quizz:
        if ox == 'O':
            conseq += 1
            score += conseq
        else:
            conseq = 0
    print(score)