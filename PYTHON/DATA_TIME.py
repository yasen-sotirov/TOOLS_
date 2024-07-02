"ДНИ И ЧАСОВЕ"   #

import datetime
from datetime import datetime



"OT ЧАСОВЕ В МИНУТИ"
# hour += minutes // 60
# minutes %= 60
# if hour > 23:
#     hour = 0
# print(f'{hour}:{minutes:02d} ч')



"ОТ МИНУТИ В ЧАСОВЕ"
# minutes = int(input())
# h = minutes // 60
# m = minutes % 60
# print(f'{h}:{m:02d} ч')



"ОТ STR В ДАТА"
# накрая се слага .date() иначе ще върне 2023-1-1 00:00:00
# date = '2023-1-1'
# print(datetime.strptime(date, "%Y-%m-%d").date())
# print(datetime.strptime(date, "%Y-%m-%d"))



"РАЗЛИКА В ДНИ МЕЖДУ ДВЕ ДАТИ"
from datetime import datetime
#
# str_dt1 = '20/10/2021 09:15'
# str_dt2 = '20/02/2022 04:25'
#
# dt1 = datetime.strptime(str_dt1, "%d/%m/%Y %H:%M")
# dt2 = datetime.strptime(str_dt2, "%d/%m/%Y %H:%M")
#
# delta = dt2 - dt1
# print(f'Difference is {delta.days} days')



"ДОБАВЯ БРОЙ ДНИ КЪМ ДАТА"
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date + timedelta(days=1)

print("Текуща дата и час:", current_date)
print("След добавяне на един ден:", new_date)











