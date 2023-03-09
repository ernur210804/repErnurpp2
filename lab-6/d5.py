color = ['1', 'Green', 'bad', 'pp2']
with open('m1.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('m1.txt')
print(content.read())