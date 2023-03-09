with open('1.txt','r') as firstfile, open('2.txt','a') as secondfile:
      
    for line in firstfile:
               

         secondfile.write(line)