import random
import string

def password_generator():
    password_length = int(input("Enter the desired length of the password (at least 8 characters): "))

    if password_length < 8:
        print("Password length should be at least 8 characters.")
        return

    has_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    has_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    has_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    all_characters = string.ascii_lowercase
    if has_uppercase:
        all_characters += string.ascii_uppercase
    if has_numbers:
        all_characters += string.digits
    if has_special_chars:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for i in range(password_length))

    print("Generated Password : ", password)

password_generator()
