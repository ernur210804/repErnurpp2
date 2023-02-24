from datetime import date, timedelta
dt = date.today()
print(f'current date: {dt}')
print(f'five days ago was: {dt-timedelta(5)}')

#Previous code

'''date=[int(a) for a in input('Enter current date: ').split('.')]
def Date(dt):   
    if dt[0]<=5:s
        if dt[1]==1:
            dt[2]-=1
            dt[1]=12
            dt[0]=30+(dt[0]-5)
        else:
            x=dt[0]-5
            dt[1]=dt[1]-1
            dt[0]=30+x
    
    else:
        dt[0]-=5
    for d in dt:
        print(d, end='.')

print('The date 5 days ago: ')
cn=Date(dt)
'''

#ALL METHODS

''' 
Класс datetime.date(year, month, day) - стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.

Класс datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - стандартное время, не зависит от даты. Атрибуты: hour, minute, second, microsecond, tzinfo.

Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.

Класс datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).

Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбинация даты и времени.

datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.

datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.

datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.

datetime.now(tz=None) - объект datetime из текущей даты и времени.

datetime.combine(date, time) - объект datetime из комбинации объектов date и time.

datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).

datetime.strftime(format) - см. функцию strftime из модуля time.

datetime.date() - объект даты (с отсечением времени).

datetime.time() - объект времени (с отсечением даты).

datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект datetime с изменёнными атрибутами.

datetime.timetuple() - возвращает struct_time из datetime.

datetime.toordinal() - количество дней, прошедших с 01.01.1970.

datetime.timestamp() - возвращает время в секундах с начала эпохи.

datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.

datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.

datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).

datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"

datetime.ctime() - см. ctime() из модуля time.
'''
        