t=int(input())
for i in range(t):
    x=int(input())
    c=0
    j=0
    while x>0:
        r=x%10
        x=x//10
        if r==4:
            c+=1
        j+=1
    print(c)
#Lucky Four