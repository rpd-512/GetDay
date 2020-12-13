leapch = 0
odday = [1,3,2,0,3,3,4,2,5,3,6,2,7,3,8,3,9,2,10,3,11,2,12,3]
day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
datech = 0
yod = 0
while(True):
    try:
        year = int(input('Enter Year(0 to 9999):'))
        if(year <= 9999)and(year >= 0):
            if(year%100 == 0):
                if(year%400 == 0):
                    leapch = 1
                else:
                    leapch = 0    
            else:
                if(year%4 == 0):
                    leapch = 1
                    
                else:
                    leapch = 0                    
            break
        else:
            print('invalid year')
            pass
    except:
        print('invalid year')
        pass
while(True):
    try:
        month = int(input('Enter Month(1 to 12):'))
        if(month > 0)and(month<13):
            for i in range (0,24,2):
                if(month == odday[i]):
                    odm = odday[i-1]
                    oddnum = odday[i+1]
                    if(leapch == 1 and odday[i] == 2):
                        oddnum = oddnum + 1
                    break
            break
        else:
            print('invalid month')
    except:
        print('invalid month')
        pass
while(True):
    try:
        date = int(input('Enter Date :'))
        if(date > (28+oddnum)):
            print('invalid date')
            pass
        else:
            break
    except:
        print('invalid Date')
        pass
print('\n'+str(date)+'/'+str(month)+'/'+str(year))
od = (year//100)%4
if(od == 1):
    yod = 5
elif(od == 2):
    yod = 3
elif(od == 3):
    yod = 1
elif(od == 0):
    yod = 0
twodigiyear = year-(year//100)*100
totleap = (twodigiyear-1)//4
totnleap = (twodigiyear-1) - totleap
ods = totnleap + totleap*2
ods = ods%7
totod = yod + ods
for i in range(0,(month-1)*2,2):
    if(odday[i] == 2 and leapch == 1):
        totod = totod+odday[i+1]+1
    else:
        totod = totod+odday[i+1]
totod = totod+(date%7)
totod = totod%7
print(day[totod])
