a="(([]))"
def valid(a):
    stack=[]
    for i in a:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
        if i==')' or i== ']' or i=='}':
            if len(stack)==0 :
                stack.append(i)
                break
            if ("{" or '[' or '(' not in stack) and (i==')' or i==']' or i=='}'):
                print(stack)
                stack.append(i)
            stack.pop()
    print(stack)
    if len(stack)==0:
        print("Yes")
    else:
        print("No")
valid(a)