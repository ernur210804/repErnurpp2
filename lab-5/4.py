import re

def text_match(text):
        patterns = '[A-Z]+[a-z]+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
text=str(input('enter the text '))
print(text_match(text))
