import os

for dirpath,dirnames,dirfiles in os.walk('/Users/Yernur/Desktop'):
    print('Current Path',dirpath)
    print('Direcories',dirnames)
    #print('Files',dirfiles)