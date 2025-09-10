"""
will give the sum, quotient, product and difference of two numbers
"""
op = input("enter the operation: ")
#two variables 
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number "))

sum = num1 + num2
diff = num1 - num2

if  op.lower == "sum":
    print(f"this is the sum: {sum}")
elif op.lower =="difference":
    print(f"this is the difference of the two numbers:{diff}")
elif op.lower =="quotient":
    print(f"this is the quotient of two numbers: (quotient)")
elif op.lower =="product":
    print(f"this is the product of the two numbers: (product)")