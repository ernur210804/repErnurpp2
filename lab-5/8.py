import re

def text_match(text):
        x= re.split("[A-Z]",text)
        return x
        
       
text=str(input('Enter the text: '))
print(text_match(text))
