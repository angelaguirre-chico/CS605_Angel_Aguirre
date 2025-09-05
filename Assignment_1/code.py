
another = True

print("Welcome to the Simple Calculator!")

while(another):

 while(True):
  try:
   num1 = float(input("Enter the first number: "))
   break
  except ValueError:
   print("This calculator only supports integers")
   continue
  except:
   print("Something went wrong")
   
 while(True):
  try:
   num2 = float(input("Enter the second number: "))
   break
  except ValueError:
   print("This calculator only supports integers")
   continue
  except:
   print("Something went wrong")
 

 while(True):
  print("Select an Operation:\n\
1. Addition\n\
2. Subtraction\n\
3. Multiplication\n\
4. Division") 
 
  try:
   operation = int(input("Enter the operation number: "))
  except ValueError:
   print("Please Enter an Integer")
   continue

  match operation:
   case 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    break
   case 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    break
   case 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    break
   case 4:
    try:
     result = num1 / num2
     print(f"{num1} / {num2} = {result}")
     break
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
