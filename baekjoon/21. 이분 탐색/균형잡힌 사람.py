while True:
    lis = []
    stack = []
    answ = True
    inp = input()

    print(inp)
    for i in inp:
        if i == "[":
            stack.append("[")
        elif i == "(":
            stack.append("(")
        elif i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                answ = False
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                answ = False

    if inp == ".":
        break
    else:
        if answ == True and not stack:
            print("yes")
        else:
            print("no")
