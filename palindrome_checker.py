print("Welcome to plaindrome checker 😁")
word = input("enter the word: ")
def is_palindrome(a):
    b = a[::-1]
    if b == a:
        return True
    else:
        return False
    
if is_palindrome(word):
    print("Yes, it is plaindrome")
else:
    print("No, it is not a palindrome")