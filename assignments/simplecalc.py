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
def addiction():
    sum = num1 + num2
    print("this is the sum")


def difference ():
    difference = num1 - num2
    print("this is the difference") 


def divide ():
   quotient = num1 
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
elif == '*':
  print(f"from holy ghost, enter bus heading to abakpa")
elif =='+':
  print(f"you have arrived to your destination")
else:
  print("invalid choice")


print("welcome to abakpa")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice!")

    # Ask user if they want to continue
    again = input("Do you want to continue? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting program. Goodbye!")
        break





























