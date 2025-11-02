def add(num1,num2):
    val = num1+num2
    return val


def substract(num1,num2):
    val = num1-num2 
    return val


def multiply(num1,num2):
    val = num1*num2 
    return val

def division(num1,num2):
    try:
        val = num1/num2
        return val 
    except ZeroDivisionError:
        print("num2 can't be zero")

