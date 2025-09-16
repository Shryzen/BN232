# making a menu driven calculator 
def calculator ():
    while True:
        print("\n---------Simple Calculator----------")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. floor division (//)")
        print("6. Modulus (%)")
        print("7. Exponentiation (**)")
        print("8. Exit")

        choice = input("Enter Your choice (1-8): ")
    
        if choice == '8':
            print("thank You for using the calculator. Good Bye (^3^)")
            break
        try:
            num1 = float(input("Enter your first number:"))
            num2 = float(input("Enter your second number:"))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print("result:", num1 + num2)
           
        elif choice == '2':
            print("result:", num1 - num2)
            
        elif choice == '3':
            print("result:", num1 * num2)
        
        elif choice == '4':
            if num2 != 0:
                print("result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
            
        elif choice == '5':
            if num2 != 0:
                print("result:", num1 // num2)
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == '6':
            if num2 != 0:
                print("result:", num1 % num2)
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == '7':
            print("result:", num1 ** num2)
        else:
            print("invalid choice!")
calculator()
