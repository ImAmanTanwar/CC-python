t=int(input())
while t>0:
    inp=input()
    l=len(inp)
    count =0
    for i in range(0,l):
        if inp[i]=='>' and i>0:
            if inp[i-1]=='<':
                count+=1
    print(count)
    t-=1
    
