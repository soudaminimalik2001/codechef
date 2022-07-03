t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    m=x*100
    m1=y*10
    if m<m1:
        print("Disposable")
    else:
        print("Cloth")
#chef and masks