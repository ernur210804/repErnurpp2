def gen(a):
    for i in range(a):
        if i%3==0 or i%4==0:
            yield i
    
a=int(input())
for num in gen(a):
    print(num)