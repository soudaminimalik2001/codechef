t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=y-x
    if z>=0:
        print(z)
    elif z<0:
        z*=-1
        # print(abs(z))
        if z%2!=0:
            print((z//2)+2)
        elif z%2==0:
            print(z//2)
#Equal Integer