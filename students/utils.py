

from datetime import datetime
a = datetime(2023,12,30)
b = datetime(2023,1,2)
z = b.day-3
if z<=b.day and b.day+27<=31:
    x = b.day+27
    m = b.month
elif z>0:
    x = z
    m = b.month+1
c = datetime(2023, m, x)
print("To'lov qilish kerak bo'lgan sana = ",c)






# e = b.month+1
# z = 0
# if e==1:
#     z = 31
# elif e==2:
#     if b.year%4==0 and b.year%100 != 0 or b.year%400==0:
#         z = 29
#     else:
#         z = 28       
# elif e==3:
#     z = 31   
# elif e==4:
#     z = 30   
# elif e==5:
#     z = 31  
# elif e==6:
#     z = 30   
# elif e==7:
#     z = 31   
# elif e==8:
#     z = 31   
# elif e==9:
#     z = 30   
# elif e==10:
#     z = 31   
# elif e==11:
#     z = 30   
# elif e==12:
#     z = 31   
# d = b.day-3
# k = b.month+1
# print(k, d)
# if d==0:
#     d = z
# if d<=31:
#     k = b.month
# print(z,d)
# c = datetime(2023,k,d)
# # print(dir(calendar))
