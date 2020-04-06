T = int(input())
for i in range(0,T):
    n = int(input())
    S = 0
    a = list(map(int,input().split()))
    for j in range(0,len(a)):
        S = S + a[j]
    print(S)
