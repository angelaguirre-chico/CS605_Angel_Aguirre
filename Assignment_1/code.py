
another = True

print("Welcome to the Simple Calculator!")

while(another):

 try:
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
 except ValueError:
  print("This calculator only supports integers")
  continue
 except:
  print("Something went wrong")
 
 print("Select an Operation:\n\
1. Addition\n\
2. Subtraction\n\
3. Multiplication\n\
4. Division")
 
 operation = int(input("Enter the operation number: "))
 
 match operation:
  case 1:
   result = num1 + num2
   print(f"{num1} + {num2} = {result}")
  case 2:
   result = num1 - num2
   print(f"{num1} - {num2} = {result}")
  case 3:
   result = num1 * num2
   print(f"{num1} * {num2} = {result}")
  case 4:
   try:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
   except ZeroDivisionError:
    print("Cant divide by 0")
   except:
    print("Something went wrong")
  case _:
   print("That is not a supported operation")

 while(True):

  response = input("Do you want to perform another calculation (yes/no): ")
 
  if response.lower() == "no":
   another = False
   print("Goodbye!")
   break
  elif response.lower() == "yes":
   break
