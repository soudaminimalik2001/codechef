t=int(input())
for i in range(t):
    x,y,p,q=map(int,input().split())
    m=x+p*10
    m1=y+q*10
    if m<m1:
        print("Chef")
    if m==m1:
        print("Draw")
    if m>m1:
        print("Chefina")
#chef and contest