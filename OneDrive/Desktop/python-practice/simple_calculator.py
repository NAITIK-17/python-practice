
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Undefined!")

def getValid_number(x):
    while True:
        try:
            num = input(x)
            return float(num)
        except:
            print("Invalid input. Please enter a valid number.")

def getValid_operator(x, y):
    while True:
        op = input(x).lower()
        if op in y or op in ['quit', 'exit']:
            return op
        else:
            print("Invalid operator, PLease use one these: +, -, *, /")

def run_calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    current_result = getValid_number(input())
    print(f"Starting with: {current_result}")
    while True:
        op = getValid_operator(input("Enter an operator: "), operations)
        if op in ['quit', 'exit']:
            print("Thank you for using Our Calculator!")
            break
        
        b = getValid_number(input())
        op_function = operations[op]
        new_result = op_function(current_result, b)
        if new_result is None and op == "/":
            continue
        elif new_result is None:
            print("Unexpected error occured during calculation.")
            continue
        print(new_result)
        current_result = new_result

if __name__ == "__main__":
     run_calculator()