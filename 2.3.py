i=1
while i<101:
    k=0
    for j in range(2,i):
        if i%j==0:
            k=1
    if k==0:
        print(i)
    i+=1
    
