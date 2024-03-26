n = int(input())
inf = 1e9
info,dp,trace = [],[],[]
for i in range(n):
    a,b = map(int,input().split())
    info.append((a,b))
    if i == 0:
        dp.append([inf]*(b-a+1))
        trace.append([-1]*(b-a+1))
    dp.append([inf]*(b-a+1))
    trace.append([-1]*(b-a+1))
 
s1,e1 = info[0]
dp[0] = [0]*(e1-s1+1)
trace[0] = list(range(s1,e1+1))
for idx,rg in enumerate(info):
    s2,e2 = rg
    for x in range(s1,e1+1):
        for nx in range(s2,e2+1):
            diff = abs(x-nx)
            if dp[idx][x-s1] + diff < dp[idx+1][nx-s2]:
                dp[idx+1][nx-s2] = dp[idx][x-s1] + diff
                trace[idx+1][nx-s2] = x
    s1,e1 = rg
 
answer = []
midx,mval = 201,inf
for idx,val in enumerate(dp[-1]):
    if val < mval:
        midx,mval = idx,val
answer.append(info[-1][0]+midx)
 
for i in range(n-1):
    answer.append(trace[-i-1][answer[-1]-info[-i-1][0]])
 
print(min(dp[-1]))
for a in answer[::-1]:
    print(a,sep = '\n')