s=str(input())

stack = []

f = True

for ch in s:
    if ch == '(' or ch == '[' or ch == '{':
        stack.append(ch)    
    else:
        if len(stack) > 0:
            if ch == ')' and stack.pop() != '(':
                f = False 
                break
            if ch == ']' and stack.pop() != '[':
                f = False 
                break
            if ch == '}' and stack.pop() != '{':
                f = False 
                break    
        else:
            f = False
            break

if len(stack) != 0:
    f = False


if f == True:
    print("Correct!")
else:
    print("Incorrect!")

    