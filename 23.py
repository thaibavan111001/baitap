a=input('nhap chuoi: ')
chu=0
so=0
for i in a:
    if i.isalpha():
        chu+=1
    else:
        so+=1
print(chu)
print(so)
