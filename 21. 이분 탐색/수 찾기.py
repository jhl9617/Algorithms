

n = int(input())
Anums = list(map(int, input().split()))
m = int(input())
Bnums = list(map(int, input().split()))
a = sorted(Anums)

for i in Bnums:
    low, high = 0, n-1
    brk = False
    while low <= high:
        mid = (low + high) // 2

        if i == a[mid]:
            print(1)
            brk = True
            break
        elif i > a[mid]:
            low = mid + 1

        else:
            high = mid - 1

    if brk == False:
        print(0)
