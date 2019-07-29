for t in range(int(input())):
    n,k,v=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    for i in range(n):
        s+=a[i]
    x=(((n+k)*v)-s)/k
    x=float(x)
    if x>0:
        if((x).is_integer()):
            print(int(x))
        else:
            print(-1)
    else:
        print(-1)