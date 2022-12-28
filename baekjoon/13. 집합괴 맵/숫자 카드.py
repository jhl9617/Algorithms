import sys
input = sys.stdin.readline


n = int(input())
numN = list(map(int, input().split()))
m = int(input())
numM = list(map(int, input().split()))
numN.sort()



for i in numM:
    start, end = 0, n-1
    brk = False
    while start <= end:
        mid = (end + start) // 2
        """print("i, mid", i, numM[mid])"""
        if i == numN[mid]:
            print(1,end=' ')
            brk = True
            break
        elif i > numN[mid]:
            start = mid + 1
        else:
            end = mid - 1 
        
    if brk == False:print(0, end=' ')

        
    