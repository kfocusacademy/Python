# The below methods built under my_calculation package 

# Add function to add two numbers 
def add(num1,num2):
    return (num1+num2)

# Substract function 
def substract(num1,num2):
    return(num1-num2)

# Multiplication
def multiply(num1,num2):
    return(num1*num2)

# Division
def division(num1,num2):
    try:
        return(num1/num2)
    except ZeroDivisionError:
        print("Zero division error")




