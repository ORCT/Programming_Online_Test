# z = (y+a)/(x+a)*100
'''
소수점을 전부 갖다 버렸을 때 어떻게 하면 z가 변할까에 대한 규칙
x범위가 10억이기 때문에 이걸 진짜 나누고 있으면 백퍼센트 시간 초과가 난다.
그러면 어떻게 해야할까

수학적으로 1의 자리가 바뀌기 위해서는 어느 정도의 변화량이 필요한지를 계산해보면 좋을 것 같다.
증가량이 총 판수의 1/100만 되면 일단 1의 자리는 바뀌는데
그게 판수가 크면 클수록 계산이 쉽지 않아진다는 거지
예를 들어서 99판에 0판이면 1판만 이겨도 1퍼가 되면서 바뀌는데
100에 0에서 1판 올라간다고 그게 바뀌냐는 거야 아니라는 거지
즉 이긴판 + 증가량/총판+증가량 을 했을 때 0.01의 변화는 있어야 바뀐다는 거고
그게 1/100이라는거지
증가량을 1/100 단위로 주어가면서 바뀌었을 때 이진 분류를 진행할까
굳이 그럴 필요가 있나? 1/100을 주면 무조건 바뀌는데
a/x+a가 0.01이 되는 순간을 찾아야 하는데
또 굳이 0.01이 될 필요가 없는게
예를 들어서 원래 값이 0.009999999.... 로 나아가는 경우가 있다고 치자
1000000000 99999999 이 때는 두 판만 해도 넘는데 
a/x+a를 0.01만들겠다고 쓰잘데기 없이 큰거 더하고 이진탐색으로 쭉쭉 내려갈 필요 없다는 거지

현재 확률을 본 다음에 필요한 만큼을 더하는 방식으로 구할 수 있을까?
정답에 도달하기에는 약간 부족한 논리다
100 80일때는 80퍼지만 이게 106으로 바뀌면 75가 되면서 6판을 해야한다는 논리에 도달하기는 이걸론 부족하다
분모가 변하면서 확률이 많이 움직이기 때문에 이걸로는 문제가 있을듯
간단하게 접근하기에 제일 좋은거는 a의 기본 단위를 x의 1/100만큼 잡고 변화가 생겼다면 이분탐색을 진행하는 쪽일까

'''
x, y = map(int, input().split())
z = y*100//x
if z >= 99:
    print(-1)
else:
    ans = 0
    t, b = x, 0
    while b < t:
        mid = (t + b)//2
        if z < (y+mid)*100//(x+mid):
            t = mid
            ans = t
        else:
            b = mid + 1
            ans = b
    print(ans)
    
'''
곱셈 순서를 바꾸니까 값이 달라졌음
'''