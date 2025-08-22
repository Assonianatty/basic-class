"""
simple calculator, that gets two user int inputs and op
returns sum, diff, quotient, product
"""

#user inputs, num1 and num2
num1 = int(input("input your first number: "))
num2 = int(input("enter your second number: "))

#operation input
op = input ("enter your operation: sum \nproduct \nquotient \ndifference ").lower()

#sum, difference, quotient, product
sum = num1 + num2
difference = num1 - num2
quotient = num1 / num2
product = num1 * num2


if(op.lower() == "sum"):
  print(f"this is the sum: (sum)")
elif (op.lower()== "difference"):
  print(f"this is the difference of the two numbers:  (difference)")
elif(op.lower() == "quotient"):
  if (num2 == 0):
      print("undefined")
  else:
   print(f"this is the quotient of two numbers: {quotient}")
elif (op.lower() == "product"):
   print(f"this is the product of two numbers: {product}")
else:
   print("invalid operator")


print ("end of program")






print("aptech to abakpa")
print("1. additional(+)= move forward")
print("2. subtraction(_)= turn back")
print("3. multiplication(*)= long route")
print("4. division(/)=shortcut")


#starting from = aptech
destination =abakpa

if choice =='+':
  print(f"from aptech, enter keke heading to holy ghost")
elif =='*':
  print(f"from holy ghost, enter bus heading to abakpa")
elif =='+':
  print(f"you have arrived to your destination")
else:
  print("invalid choice")


print("welcome to abakpa")