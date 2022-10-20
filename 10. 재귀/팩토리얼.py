def funcc(n):
    result = 1
    if n > 0:
        result = n * funcc(n-1)
    return result


n = int(input())
print(funcc(n))