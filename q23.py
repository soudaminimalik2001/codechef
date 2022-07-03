t=int(input())
for i in range(t):
    p_a,p_b,q_a,q_b=map(int,input().split())
    m=max(p_a,p_b)
    m1=max(q_a,q_b)
    # m2=max(m,m1)
    if m<m1:
        print("P")
    if m>m1:
        print("Q")
    if m==m1:
        print("TIE")
#DETERMINE THE WINNER