import string
import random

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    special_chars = input("Include special characters (yes/no): ").strip().lower()
    use_special_chars = special_chars == 'yes'

    if length < 1:
        print("Password length must be at least 1.")
    else:
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
