import re


def spaces(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

txt=str(input("Enter the text: "))
print(spaces(txt))
