import random
import string

def check_password_strength(password):
    length_ok = len(password) >= 8
    has_digits = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special_chars = any(char in string.punctuation for char in password)

    if length_ok and has_digits and has_uppercase and has_special_chars:
        return True
    else:
        return False

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        print("1. Check password strength")
        print("2. Generate new password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter the password: ")
            if check_password_strength(password):
                print("Password is strong")
            else:
                print("Password is weak")
        elif choice == "2":
            length = int(input("Enter the desired password length: "))
            new_password = generate_password(length)
            print(f"Generated password: {new_password}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()