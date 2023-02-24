import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)
tomorrow=today+datetime.timedelta(1)
print(f'Yesterday was: {yesterday}')
print(f'Today is: {today}')
print(f'Tomorrow will be: {tomorrow}')
