t=int(input())
for j in range(t):
    n=int(input())
    la=list(map(int,input().split()))
    ld=list(map(int,input().split()))
    a=[];d=[]
    for k in range(n):
        a.append(la[k])
        d.append(ld[k])
    t=[]     
    flag=0              
    for i in range(0,n):       
        if i!=n-1 and d[i]>a[i+1]+a[i-1]:
            t.append(d[i])
            flag=1
        elif i==n-1 and d[i]>a[0]+a[i-1]:
            t.append(d[i])
            flag=1
        elif i==n-1 and d[i]<=a[0]+a[i-1]:
            if (flag!=1):
                print('-1')
        if flag==1: 
            if i==n-1:
                print(max(t))