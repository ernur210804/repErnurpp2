import time

def sqTime(n,t):
    time.sleep(t/1000)
    return (n**0.5)

n=int(input("Enter second: "))
t=int(input('Enter msecond: '))
d=sqTime(n,t)
print(f'Square root of {n} after {t} miliseconds is {d}')