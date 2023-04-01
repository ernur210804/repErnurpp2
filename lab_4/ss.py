import re
p='^[A-Z].*[a-z]$'
txt=str(input('enter your txt:'))
if re.search(p,txt):
    print('yes')
else:
    print('no')