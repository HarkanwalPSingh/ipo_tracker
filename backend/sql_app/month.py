import calendar
from datetime import date

MONTHS = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6,
          "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def last_date_of_month(year:int,month:str):
    _end_date = calendar.monthrange(year,MONTHS.get(month))[1]
    print(_end_date)
    return (date(year=year,month=MONTHS[month],day=1),date(year=year,month=MONTHS[month],day=_end_date))

# print(last_date_of_month(2022,"June"))