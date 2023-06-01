def bracket(open,close):
    if open=="[" and close=="]":
        return True
    if open=="(" and close=="(":
        return True
    if open=="{"and close=="}":
        return True
    return False

def balance(expr):
    stack=[]
    for i in range(len(expr)):
        if expr[i]=="[" or expr[i]=="(" or expr[i]=="{":
            stack.append(expr[i])
        elif expr[i]=="]" or expr[i]==")" or expr[i]=="}":
            if bracket (stack[-1 ],expr[i] or len(stack)!=0):
                stack.pop()
                
            else:
               return False
            if len(stack)==0:
                return True
            else:
                return False

expr=input("Enter the value")
print("the given expression is %s" %balance(expr))
