count=0
for i in range(1,6):
    if i%2!=0:
        for j in range(count+1,count+i):
            print(j,end='')
        j=count+i
        print(j)
        j+=1
        count=j
    else:
        count=count+i-1
        for j in range(count,count-i+1,-1):
            print(j,end='')
        j=count-i+1
        print(j)
    

