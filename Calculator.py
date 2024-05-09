import os, sys
print("--Calculator--")
result = int(input("Enter a Numbers: "))
while True:
    os.system("clear")
    print("--Calculator--")
    print("\nResult : ",result,"\n")
    choice = input("Addition\nSubtraction\nMultiplication\nDivision\nExit\n\nEnter Your Choice : ")
    if choice in ["Exit",'EXIT','EXIT','exit','Exit','e','E']:
      os.system("clear")
      sys.exit(f"--END--\n\nRESULT : {result}")
    else:
      y = int(input("Enter Number : "))
      if choice in ["Addition",'ADDITION','ADD','add','Add','+','addition']:
        result += y
        print("\nResult : ",result)
      elif choice in ["Subtraction",'SUBTRACTION','SUB','sub','Sub','-','subtraction']:
        result -= y
        print("\nResult : ",result)
      elif choice in ["Multiplication",'MULTIPLICATION','MUL','mul','Mul','*','multiplication']:
        result *= y
        print("\nResult : ",result)
      elif choice in ["Division",'DIVISION','DIV','div','Div','/','division']:
        result /= y
        print("\nResult : ",result)
  
