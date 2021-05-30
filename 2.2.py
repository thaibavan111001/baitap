for i in range(0,101):
    k=1
    for j in range(2,i):
        if i%j==0:
            k=0
    if k==1:
        print(i)
   
        
