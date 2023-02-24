def my_range(a):
    for i in range(a):
        i+=1
        yield i**2

        

a=int(input())
for num in my_range(a):
    print(num)
        