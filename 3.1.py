def giai_thua(a):
    n='1,'
    k=1
    for i in range(2,a+1):
        k=k*i
        n=n+str(k)+","
    return n
so=int(input('Nhap so can tinh: '))
print(giai_thua(so))
