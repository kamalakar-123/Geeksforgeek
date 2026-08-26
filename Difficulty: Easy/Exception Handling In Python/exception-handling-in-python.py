def find_minimum(a, b):
    # code here  
    try:
        sum1=a+b
        sub1=a-b
        mul=a*b
        div=a//b
        
    except ZeroDivisionError:
        return  min(sum1,sub1,mul)
    else:
        return min(sum1,sub1,mul,div)
        