t=int(input())
i=0
while i<t:
    x,y,z=map(int,input().split())
    if y>x>z or z>x>y:
        print(x)
    elif x>y>z or x<y<z:
        print(y)
    else:
        print(z)
    i+=1
#Second Max of Three Numbers