# find next day
day=29
month=2
year=2025
if day==31 and month==12:
    day=1
    month=1
    year+=1
elif day==30 and (month==4 or month==6 or month==9 or month==11):
    day=1
    month+=1
elif day==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 ):
    day=1
    month+=1
elif month==2 and (day==28 or day==29 ):
    if year%400==0 or (year%100!=0 and year%4==0) :
        if day==28:
            day+=1
        else:
            day=1
            month+=1
    else:
        # if day==29:
        #     print("invalid date ")
        #     day=1
        #     month+=1
        # else:
            day=1
            month+=1
else:
    day+=1

print(f"day= {day} month= {month} year= {year}")