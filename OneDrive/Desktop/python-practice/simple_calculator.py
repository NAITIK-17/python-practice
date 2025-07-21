def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def get_num(x):
    while True:
        try:
            num = input(x)
            return float(num)
        except ValueError:
            print("use a valid number")

def get_op(x, y):
    while True:
        try:
            op = input(x)
            if op in y or op in ['quit', 'exit']:
                return op
        except:
            print("Invalid Operator: PLease use valid operator like, +, -, *, /")

def run_calculator():
    print("when asked input always enter first then write, even if it is first input")
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    a = get_num(input("Enter a number: "))
    while True:
        op1 = get_op(input("Enter an operator: "), operations)
        if op1 in ['quit', 'exit']:
            print("Thank you for using our calculator!")
            break
        
        b = get_num(input("Enter a number: "))
        op_func = operations[op1]
        result = op_func(a, b)
        print(result)
        a = result



if __name__ == "__main__":
    run_calculator()