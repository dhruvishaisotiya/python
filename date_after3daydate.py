# input date and find after 3 day date
day=28
month=2
year=2025
u=3
for i in range(1,u+1):
        if day==31 and month==12:
            year+=1
            month=1
            day=1
        elif day==30 and (month==4 or month==6 or month==9 or month==11):
            month+=1
            day=1
        elif day==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            month+=1
            day=1
        elif month==2 and (day==28 or day==29):
            if year%400==0 or (year%100!=0 and year%4==0):
                if day==28:
                    day+=1
                else:
                    day=1
                    month+=1
            else:
                if day==28:
                    day=1
                    month+=1
                else:
                    print("invalid date")
                    day=1
                    month+=1
        else:
            day+=1

print(f"day = {day} ,month= {month} , year= {year}")
