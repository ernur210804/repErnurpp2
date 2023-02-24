import re

def text_match(text):
         return ''.join(x.capitalize() or '_' for x in text.split('_'))
        
       
text=str(input('Enter the text: '))
print(text_match(text))
