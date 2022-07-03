t=int(input())
i=0
while i<t:
    n,d,p=map(int,input().split())
    s=d*p
    if s>=n:
        print("YES")
    else:
        print("NO")
    i+=1
#tyre problem