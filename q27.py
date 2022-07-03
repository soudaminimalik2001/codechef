t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%k==0:
        print(n//k)
    else:
        print(-1)
#can you eat it