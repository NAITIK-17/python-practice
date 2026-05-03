#Bill Spliter
print("Welcome To Franco's Dinner!")
while True:
    print('=' * 45)
    total_bill = float(input("Enter the total amount of bill: "))
    print('-' * 45)

    if total_bill <= 0:
        print("Be True To Yourself.")
        print("=" * 45)
        continue

    persons = int(input("No. of people incl. you: "))
    print('-' * 45)

    if persons <= 0:
        print("am I Blind!!!!!")
        print("=" * 45)
        continue
    
    tip = float(input("Tip %: "))
    tip_amount = (total_bill) * (tip/100)
    total_amount = total_bill + tip_amount
    
    print("=" * 45)
    
    bill_per_person = ( total_amount / persons )
    
    print(f"So, bill per person is ${bill_per_person:.2f}")
    print("Thank You! Visit Us Again.")
    print("=" * 45)
    break
