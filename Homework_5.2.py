while True:
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    plusminus = input("Enter +, -, * or /")

    match plusminus:
        case "+":
            print(number1+number2)
        case "-":
            print(number1-number2)
        case "*":
            print(number1*number2)
        case "/":
            if number2 == 0:
                print("error, you cant divide on zero")
            else:
                print(number1/number2)
        case _:
            print("error, invalid type of symbol")

    user_input = input("Would you like to continue calculations yes/no:" )
    if user_input == "yes" or user_input == "y":
        continue
    elif user_input == "Yes" or user_input == "Y":
        continue
    elif user_input == "no" or user_input == "n":
        break
    elif user_input == "No" or user_input == "N":
        break
    else:
        print("Incorrect input. Please choose correct answer")
        break





