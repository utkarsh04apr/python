t=int(input())
lst=[[]]
for i in range(t):
    n=int(input())
    lst=[int(i) for i in input().split()]
    print(sum(lst))
