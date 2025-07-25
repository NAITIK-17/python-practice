import random
import string

def generate_password():
    while True:
        try:
            a = int(input("Enter length of your password:"))
            if a <= 0:
                print("Enter positive number")
            else:
                break
        except ValueError:
            print("Enter valid number")

    b = input("upper case? (y/n): ") == "y"
    c = input("lower case? (y/n): ") == "y"
    d = input("digits? (y/n): ") == "y"
    e = input("upper case? (y/n): ") == "y"   
    user_chars = ""
    if b:
        user_chars += (random.choice(string.ascii_uppercase))
    if c:
        user_chars += (random.choice(string.ascii_lowercase))
    if d:
        user_chars += (random.choice(string.digits))
    if e:
        user_chars += (random.choice(string.punctuation))

    password = random.choices(user_chars, k = a)
    random.shuffle(password)
    final_password = "".join(password)
    return final_password

if __name__ == "__main__":
    print(generate_password())
