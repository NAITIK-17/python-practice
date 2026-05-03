n = int(input("No. of terms in the sequence: "))
l = []
for i in range(n+1):
    if i == 0:
        l.append(i)
    elif i == 1:
        l.append(i)
    else:
        i = l[-2] + l[-1]
        l.append(i)
    
print(f"Your Sequence: {l}")