n = int(input("Enter rows: "))
for i in range(n):                    # range(n) instead of hardcoded 5
    x = (" " * (n-i-1)) + ("*" * ((2*i)+1))  # Fixed formula
    print(x)
