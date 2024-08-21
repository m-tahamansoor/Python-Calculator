def calculate():
    try:
        calculation = input("Enter your equation : ")
        result = eval(calculation)
        print(f"The result is: {result}")

    except(SyntaxError, NameError, ZeroDivisionError):
        print("INVALID INPUT!!! Please enter a valid arithmetic expression...")

    again = input("Further calculation? (Y or N)").upper()
    if again == "Y":
        calculate()
    else:
        print("take care :)")

calculate()