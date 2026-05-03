import os
import random

# Helper: Read account as dictionary (handles ALL file errors)
def read_account():
    if not os.path.exists('acc_detail.txt'):
        return None
    
    try:
        with open('acc_detail.txt', 'r') as f:
            lines = f.readlines()
        
        return {
            'acc': lines[0].split(': ')[1].strip(),
            'name': lines[1].split(': ')[1].strip(),
            'pin': int(lines[2].split(': ')[1].strip()),
            'balance': int(lines[3].split(': ')[1].strip())
        }
    except:
        return None

# Helper: Save account dictionary to file
def save_account(acc):
    with open('acc_detail.txt', 'w') as f:
        f.write(f"Account Number: {acc['acc']}\n")
        f.write(f"Name: {acc['name']}\n") 
        f.write(f"Pin: {acc['pin']}\n")
        f.write(f"Balance: {acc['balance']}\n")

def create_account():
    name = input("Enter username: ")
    while True:
        try:
            pin = int(input("Create 6-digit PIN: "))
            if 100000 <= pin <= 999999:
                break
            print("PIN must be 6 digits")
        except:
            print("Enter valid number")
    
    acc_num = str(random.randint(10000000, 99999999))  # 8 digits
    acc = {'acc': acc_num, 'name': name, 'pin': pin, 'balance': 0}
    save_account(acc)
    print(f"✅ Account created! Number: {acc_num}")

def home_page(acc):
    print("\n" + "="*40)
    print(f"👋 Welcome {acc['name']}!")
    print(f"💰 Balance: ₹{acc['balance']}")
    print("1. Deposit  2. Withdraw  3. Payment  4. Exit")
    print("="*40)

def deposit(acc):
    try:
        amount = int(input("Enter deposit amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive")
            return
        acc['balance'] += amount
        save_account(acc)
        print(f"✅ Deposited ₹{amount}. New balance: ₹{acc['balance']}")
    except:
        print("❌ Enter valid number")

def withdraw(acc):
    try:
        amount = int(input("Enter withdraw amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be positive")
            return
        if amount > acc['balance']:
            print("❌ Insufficient funds")
            return
        acc['balance'] -= amount
        save_account(acc)
        print(f"✅ Withdrew ₹{amount}. New balance: ₹{acc['balance']}")
    except:
        print("❌ Enter valid number")

def run():
    acc = read_account()
    
    if not acc:
        print("👤 No account found. Creating new account...")
        create_account()
        return
    
    # Login
    print("🔐 Login:")
    username = input("Username or Account Number: ")
    try:
        pin = int(input("PIN: "))
    except:
        print("❌ Invalid PIN")
        return
    
    if (username == acc['name'] or username == acc['acc']) and pin == acc['pin']:
        while True:
            home_page(acc)
            try:
                choice = int(input("Choose (1-4): "))
                match choice:
                    case 1:
                        deposit(acc)
                    case 2:
                        withdraw(acc)
                    case 3:
                        print("⏳ Payment under development")
                    case 4:
                        print("👋 Thank you! Exited.")
                        break
                    case _:
                        print("❌ Choose 1-4 only")
            except:
                print("❌ Enter valid choice")
    else:
        print("❌ Invalid credentials")

if __name__ == "__main__":
    run()
