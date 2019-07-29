for t in range(int(input())):
    n=int(input())
    a=input().split(' ')
    b=a[1]
    l=a[0].split(b)
    m=len(a[0])
    n1=m*(m+1)*0.5
    n2=0
    for i in range(len(l)):
        k=len(l[i])
        n2+=(k*(k+1)*0.5)
    print(int(n1-n2))