#sum of w <= k, print max v
#brute force or backtracking

'''
First solve, but it cannot pass all test case

import sys
ssr = sys.stdin.readline

n,k = map(int, ssr().split())
things = [list(map(int, ssr().split())) for i in range(n)]
things.sort(key=lambda x : -(x[1]/x[0]))#coefficient of value/weight
max_value = []
for i in range(n):
    #sum_w = 0
    #sum_v = 0
    sum_w = things[i][0]
    sum_v = things[i][1]
    for j in range(i+1,n):
        if sum_w + things[j][0] > k:
            continue
        else:
            sum_w += things[j][0]
            sum_v += things[j][1]
    max_value.append(sum_v)
print(max(max_value))
'''

'''
Second solve, backstracking but it occured time out

def func(i):
    global sum_w
    global sum_v
    if sum_w > k:#방금전에 수행한거 빼고 출력하고
        sum_w -= things[i-1][0]
        sum_v -= things[i-1][1]
        value.append(sum_v)
        return
    elif sum_w == k:
        value.append(sum_v)
        return
    for i in range(n):
        if not check[i]:
            sum_w += things[i][0]
            sum_v += things[i][1]
            check[i] = True
            func(i+1)
            check[i] = False
    sum_w = 0
    sum_v = 0

import sys
ssr = sys.stdin.readline

n,k = map(int, ssr().split())
check = [False for _ in range(n)]
things = [list(map(int, ssr().split())) for i in range(n)]#not need sort in backtracking
value = []
sum_w = 0
sum_v = 0
func(0)
print(max(value))
'''