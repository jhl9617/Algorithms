while (True):
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    elif N % M == 0:
        print('multiple')
    elif M % N == 0:
        print('factor')
    else:
        print('neither')
