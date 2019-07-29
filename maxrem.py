n=int(input())
a=list(set(map(int,input().split())))
a.sort()
if(len(a)==1):
    print(a[-1]%a[-1])
else:
    print(a[-2]%a[-1])