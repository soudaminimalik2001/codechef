t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    m=y*30
    if m<=x:
        print("YES")
    else:
        print("NO")
#budget monthly