import re

def text_match(text):
        return re.sub("[ ,.]",';',text)
        
       
text=str(input('enter the text '))
print(text_match(text))
