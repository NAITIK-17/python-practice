import random
import math

def get_coefficients():
    a = float(input("Enter first coefficient: "))
    b = float(input("Enter second coefficient: "))
    c = float(input("Enter third coefficient: "))
    return a, b, c

def poly_type(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "zero polynomial"
            else:
                return "constant polynomial"
        else:
            return "linear polynomial"
    else:
        return "quadratic polynomial"

def find_roots(a, b, c):
    poly_type_result = poly_type(a, b, c)
    if poly_type_result == "linear polynomial":
        if b != 0:
            alpha = -c/b
            print(f"Root: {alpha}")
    elif poly_type_result == "quadratic polynomial":
        discremenate = b**2 - 4*a*c
        if discremenate >= 0:
            alpha = (-b + math.sqrt(discremenate))/(2*a)
            beta = (-b - math.sqrt(discremenate))/(2*a)
            print(f"Roots: {alpha}, {beta}")

def root_relation(a, b, c):
    relation = input("What you want to find: ")
    relation = relation.lower()
    if relation == "sor":
        sor = -b/a
        return sor
    elif relation == "por":
        por = c/a
        return por

def generate_polynomial():
    print("If no alpha beta, just press enter key without writing anything")
    alpha = input("Enter value of alpha: ")
    beta = input("Enter vale of beta:  ")
    if alpha == "" and beta == "":
        number_of_poly = int(input("Enter number of polynomial you want: "))
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = random.randint(1,10)
        sor = -b/a
        por = c/a
        print(f"{a}x**2 {'+' if b >= 0 else ''}{b}x {'+' if c >= 0 else ''}{c}")
    else:
        sor = int(alpha) + int(beta)
        por = int(alpha) * int(beta)
        print(f"x**2 -{sor}x + {por}")

def check_x_value(a, b, c):
    x_value = int(input("Enter value of x: "))
    p = (a*(x_value)**2) + (b*(x_value) + c)
    print(f"polynomial: f(x) = {a}x**2 + {b}x + {c}")
    print(f"for p({x_value}) = {p:.4f}")

def run_polynomial_solver():
    ask = input("Choose options:\n1.)Find roots\n2.)root relations\n3.)generate polynomial\n4.)value of x for p(x) = 0\nYour choice: ")
    ask = ask.lower()
    if ask == "find roots":
        a, b, c = get_coefficients()
        find_roots(a, b, c)
    elif ask == "root relations":
        a, b, c = get_coefficients()
        root_relation(a, b, c)
    elif ask == "generate polynomial":
        a, b, c = get_coefficients()
        generate_polynomial()
    elif ask == "value of x for p(x) = 0":
        a, b, c = get_coefficients()
        check_x_value(a, b, c)
    else:
        print("option not available")

if __name__ == "__main__":
    run_polynomial_solver()