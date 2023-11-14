import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length)) #Run length times
    return password


password_length = int(input("Enter the length of the password (default is 12): "))

if password_length <= 0:
        print("Invalid length. Using default length (12).")
        password_length = 12
        
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
