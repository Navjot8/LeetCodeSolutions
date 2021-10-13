date = "6th Jun 1933"
"2052-10-20"
newDate=date.split()
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month=str(months.index(newDate[1])+1)
if len(month)!=2:
    month="0"+month
day=newDate[0][:len(newDate[0])-2]
if len(day)!=2:
    day="0"+day
reformatedDate=newDate[2]+"-"+month+"-"+day
print(reformatedDate)

