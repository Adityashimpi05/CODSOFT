import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define the character sets to choose from
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase + lowercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to ensure random distribution
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                raise ValueError("Password length should be at least 8 characters.")
            password = generate_password(length)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)
        
        another = input("Generate another password? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
