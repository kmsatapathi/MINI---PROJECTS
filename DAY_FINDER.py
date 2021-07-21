def check_leap(y):
    if y%100==0:
        if y%400==0:            # function to check leap year.
            return 1
        else:
            return 0
    else:
        if y%4==0:
            return 1
        else:
            return 0
print("....ENTER DATE IN BELOW FORMAT....\ndd mm yyyy")
l=list(map(int,input().split()))
d=l[0];m=l[1];y=l[2];
d_no={}
l1=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']          # day no.
for i in range(0,7):
    d_no[i]=l1[i]

m_no={1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5} #month no.
if y>=1600 and y<=1699:
    y_no=6
elif y>=1700 and y<=1799:
    y_no=4
elif y>=1800 and y<=1899:
    y_no=2
elif y>=1900 and y<=1999:       # year no.
    y_no=0
elif y>=2000 and y<=2099:
    y_no=6
s=0
s=d+m_no[m]+y_no
val=int(str(y)[2:])   # calculating formula.
s+=val
s+=int(val/4)
res=s%7
if(check_leap(y)):
    if m<=2:
        if res==0:
            res=7
        print(d_no[res-1])
    else:
        print(d_no[res])
else:                       
    print(d_no[res])
    
# FORMULA : res = {d + m_no + y_no + (last two digits of yr) + quotient[(last two digits of yr)/4)]} % 7
print("....... DAY_FINDER PRGRAM TERMINATED .......")