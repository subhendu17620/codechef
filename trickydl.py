for t in range(int(input())):
    a=int(input())
    profit=0
    i=1
    l=[]
    d=[]
    while profit>=0:
        profit+=a-pow(2,i-1)
        l.append(profit)
        d.append(i)
        i+=1
    d1=max(d)-1
    h=max(l)
    d2=l.index(h)+1
    print("{} {}".format(d1,d2))