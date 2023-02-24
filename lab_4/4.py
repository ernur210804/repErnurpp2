import datetime
d=int(input('Enter how many days difference: '))
dt1=datetime.datetime.today().replace(microsecond=0)
dt2=dt1-datetime.timedelta(d)
sum=dt1-dt2
a=sum.total_seconds()
print(f'Difference in seconds: {a}')
print(f'Current date is {dt1}'), 