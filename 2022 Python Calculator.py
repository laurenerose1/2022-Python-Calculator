while True:
    #Divider
    print("\n-------------------------------------------------\n")
    #creating an input variable and instructions. Stop will end program
    input1 = input("Enter a number, or type STOP to turn off the calculator: ")
    #check to see if input is word STOP, Numbers or invalid
    if input1 == "STOP":
        break
    elif not input1.isdigit(): #isdigt checks to see if input is a digit
        print(" OOPS! That is not a valid number.")
        continue
    else:
        number1 = int(input1.strip())
  #op will represent opererations
    op = input("Please select an operation (+, -, *, /, or %): ")
    op = op.strip()
  
    input2 = input(" Please enter another number: ")

    if not input2.isdigit():
        print("Oops! That is not a valid number.")
        continue
    else:
        number2 = int(input2.strip())

    if op == "+":
        ans = number1+number2
    elif op == "-":
        ans = number1-number2
    elif op == "*":
        ans = number1*number2
    elif op == "/":
        ans = number1/number2
    elif op == "%":
        ans = number1%number2
    else:
        print("You did not enter a valid operation. Try again!")
        continue

    #print full equation
    print(number1, op, number2, "=", ans)