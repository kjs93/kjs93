def cal(a,b,vay):
    if vay == "+":
        return a+b
    elif vay == "*":
        return a*b
    elif vay == "-":
        return a-b
    elif vay == "/":
        if b == 0:
            return -1
        else:
            return a/b
    else:
        return 0

data=cal(2,0,'/')
print(data)
