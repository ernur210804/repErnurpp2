s=str(input())
cntUP=0
cntLW=0
for ch in s:
    if ch.isalpha():
        if ch.isupper()==True:
            cntUP+=1
        else:
            cntLW+=1
print(f"The quantity of Uppercase:{cntUP}")
print(f"The quantity of Lowercase:{cntLW}")