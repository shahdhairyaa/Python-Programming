# Simple Calculator in Python

def prompt_menu():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Division
    """)
    op = int(input("Enter the choice of number to calculate: "))
    return a, b, op

def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))
    elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
    elif op == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))
    elif op == 4:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible!")
    else:
        print("No such choice!")
    
calculate()

