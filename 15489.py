t = [[0 for _ in range(31)] for _ in range(31)]
t[1][1] = 1
for i in range(2,31):
    for j in range(1,31):
        t[i][j] = t[i-1][j-1] + t[i-1][j]
r,c,w = map(int, input().split())
answer = 0
for i in range(w):
    for j in range(i+1):
        answer += t[r+i][c+j]
print(answer)