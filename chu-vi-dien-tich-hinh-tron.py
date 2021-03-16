import math
def Tinh(R):
    if R>0:
        s=math.pi*R**2
        c=2*math.pi*R
        print("dien tich la", s)
        print("chu vi la", c)
    else:
        print("ban kinh dau vao ko hop le")
R=int(input("nhap ban kinh:" ))
Tinh(R)

