t=int(input())
s=[]
se=set()
for i in range(t):
    n=int(input())
    for j in range(n):
        s.append(set(input()))
    se=s[0]
    for k in range(1,n):
        se=se.intersection(s[k])
    print(len(se))
    se=set()
    s=[]