try:
    num1 = float(input("Welcome to my calculator. Please type the first number: "))
    operator = input("Now type the operator: ")
    num2 = float(input("Lastly, type the second number: "))

    def multiplication(x, y):
        print(x * y)

    def addition(x, y):
        print(x + y)

    def subtraction(x, y):
        print(x - y)

    def division(x, y):
        print(x / y)

    if operator == "*":
        multiplication(num1, num2)
    elif operator == "+":
        addition(num1, num2)
    elif operator == "/" or operator == ":":
        try: 
            division(num1, num2)
        except ZeroDivisionError:
            print("division by zero not feasible")
    elif operator == "-":
        subtraction(num1, num2)
    else:
        print("Operator provided not recognized. Please try something like '+' or '*' ")

except ValueError:
    print("Error: Please enter numeric values for numbers.")
