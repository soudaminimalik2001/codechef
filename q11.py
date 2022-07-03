t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    s=n*x
    if s<=k:
        print("YES")
    else:
        print("NO")
#Chef gives Party