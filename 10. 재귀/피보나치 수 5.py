def funcc(n):

    if n <= 1:
        return n

    return funcc(n-1) + funcc(n-2)

n = int(input())
print(funcc(n))