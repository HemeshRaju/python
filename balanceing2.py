a="(([]})"
def vaild(a):
    map={"(":")","{":"}","[":"]"}
    b=['(','{','[']
    stack=[]
    for i in a:
          if i=='[' or i=='{' or i=='(':
            stack.append(i)
          if i==')' or i== ']' or i=='}':
              if len(stack)==0:
                  return 'No'
              stack.pop()
    if len(stack)==0:
        return 'yes'
    else:
        return 'No'
              
print(vaild(a))
              
              
        
