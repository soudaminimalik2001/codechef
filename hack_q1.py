from re import M


t=int(input())
m=1
m1=1
for i in range(t):
    a,b=map(int,input().split())
    m=a*m
    m1=b*m1
print(m)
print(m1)
j=1
while j>=0:
    if m%j==0 and m1%j==0:
        print(j)
    j+=1
    
    