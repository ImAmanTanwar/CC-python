inp=input()
l=len(inp)
t=int(input())
val=[]
val.append(inp)
while t>0:
    mem=""
    q=input().split()
    if int(q[0])==1:
        x,y=int(q[1]),int(q[2])
        for i in range(x,y+1):
            mem+=inp[i]
        for i in range(0,x):
            mem+=inp[i]
        for i in range(y+1,l):
            mem+=inp[i]
        val.append(mem)
    elif int(q[0])==2:
        x,y=int(q[1]),int(q[2])
        for i in range(0,x):
            mem+=inp[i]
        for i in range(y+1,l):
            mem+=inp[i]
        for i in range(x,y+1):
            mem+=inp[i]
        val.append(mem)
    elif int(q[0])==4:
        x,y=int(q[1]),int(q[2])
        while x>0:
            if val[x] is not None:
                break
            x-=1
        print((val[x])[y])
        val.append(None)
    else:
        x=int(q[1])
        n=len(val)
        while n>0:
            if val[n-1] is not None:
                break
            n-=1
        print((val[n-1])[x])
        val.append(None)
    t-=1
