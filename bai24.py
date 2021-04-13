chuoi=input('nhap chuoi:')
tong_chu_thuong=0
tong_chu_hoa=0
for i in chuoi:
    if i.islower():
        tong_chu_thuong+=1
    else:
        tong_chu_hoa+=1
print('tong chu hoa la: ',tong_chu_hoa)
print('tong chu thuong la: ',tong_chu_thuong)
