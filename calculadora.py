
import math

# This function get a value from the user and validate it (it's a number or no)
def get_input(prompt):
    while True:
        number = input(prompt)
        if "." in number:
            try:
                value = float(number)
                break
            except:
                print("Sorry, I only operate with numbers.")
                continue
        else:
            try:
                value = int(number)
                break
            except:
                print("Sorry, I only operate with numbers.")
                continue
    return value

def suma():
    num1 = get_input("First number: ")
    num2 = get_input("Second number: ")
    if num1 % 1 != 0 or num2 % 1 != 0:
        print(f"{num1} + {num2} = {round((num1+num2),2)}")
    else:
        print(f"{num1} + {num2} = {num1+num2}")

def resta():
    num1 = get_input("First number: ")
    num2 = get_input("Second number: ")
    print(f"{num1} - {num2} = {round((num1-num2),2)}")

def multiplica():
    num1 = get_input("First number: ")
    num2 = get_input("Second number: ")
    print(f"{num1} * {num2} = {round((num1*num2),2)}")

def divide():
    num1 = get_input("First number: ")
    num2 = get_input("Second number: ")
    if num2 == 0:
        print("You cannot divide by zero!")
        return
    print(f"{num1} / {num2} = {round((num1/num2),2)}")

def potencia():
    num1 = get_input("The number: ")
    num2 = get_input("The power to raise at: ")
    print(f"{num1} ** {num2} = {round((num1**num2),2)}")

def raiz():
    num = get_input("The number to extract the square root from: ")
    if num < 0:
        print("Square root cannot be extracted from a negative number")
    else:
        print(f"The square root of {num} = {round(math.sqrt(num),2)}")

def bin_to_dec():
    num = input("The binary number to convert to decimal: ")
    print(f"The decimal representation of {num} is {int(num, 2)}")

def dec_to_bin():
    num = int(input("The decimal number to convert to binary (integer): "))
    binar = format(num, "b")
    print(f"The binary representation {num} is {binar}")

print("""1 Addition
2 Substraction
3 Multiplication
4 Division
5 Raise to power
6 Square root
7 Convert decimal to binary
8 Convert binary to decimal
(use '.' for float numbers)\n""")

while True:
    op = input("Choose an operation (by entering the corresponding number or 0 to exit): ")
    if op == '1':
        suma()
    elif op == '2':
        resta()
    elif op == '3':
        multiplica()
    elif op == '4':
        divide()
    elif op == '5':
        potencia()
    elif op == '6':
        raiz()
    elif op == '7':
        dec_to_bin()
    elif op == '8':
        bin_to_dec()
    elif op == '0':
        break
    print()
