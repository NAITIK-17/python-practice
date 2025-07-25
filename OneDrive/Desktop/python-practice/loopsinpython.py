b = input("while or for?: ")
b = b.lower()
if b == "for":
    a = int(input("Enter a number: "))
    
    for i in range(1, 11): 
        print(f"{a} x {i} = {a*i}")
    
    c = int(input("Number to check if prime: "))
    
    for i in range(0 , c):
        if c % 1 == 0 and c % c == 0:
            print(f"{c} is a prime number")
            break
        else:
            print(f"{c} is not a prime number")
            break

    a = input("Enter nth term: ")
    
    for i in range(0, int(a)):
        sum = i + (i + 1)
        i += 1
        print(f"S(n) = {sum}")

elif b == "while":
    a = int(input("Enter a number"))
    i = 1
    while(i<11):
        print(f"{a} x {i} = {a*i}")
        i += 1
    
    c = int(input("Enter a number to check if prime: "))
    i = 1
    while(i <= c):
        if c % i == 0 and c % c == 0:
            print(f"{c} is a prime number")
            i += 1
            break
        else:
            print(f"{c} is not a prime number")
            break

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if (name.startswith("S")):
        print(f"Hello {name}")
