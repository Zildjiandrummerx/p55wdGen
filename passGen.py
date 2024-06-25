import random, string, hashlib, datetime, os

def generate_password(length):
    if length < 12 or length > 50:
        raise ValueError("Password length must be between 12 and 50 characters")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_passphrase(word_count):
    if word_count < 3 or word_count > 10:
        raise ValueError("Passphrase word count must be between 3 and 10 words")
    
    words = ["correct", "horse", "battery", "staple", "sample", "passphrase", "generator", "random", "secure", "words"]
    passphrase = ' '.join(random.sample(words, word_count))  # Use random.sample to avoid repetition
    
    return passphrase

def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def read_pepper_from_file(filename):
    try:
        with open(filename, 'r') as file:
            pepper = ''.join([line[0] for line in file if line.strip()])
        return pepper
    except FileNotFoundError:
        print(f"Pepper file '{filename}' is missing.")
        create_pepper_file(filename)
        print(f"Created a new pepper file: '{filename}'")
        with open(filename, 'r') as file:
            pepper = ''.join([line[0] for line in file if line.strip()])
        return pepper

def create_pepper_file(filename):
    lines = [''.join(random.choices(string.ascii_letters + string.digits, k=100)) for _ in range(50)]
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

def main():
    print("Do you want a password or a passphrase? (Enter 'password' or 'passphrase')")
    choice = input().strip().lower()

    salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))  # Generate a random salt
    pepper_filename = "pepper.txt"
    pepper = read_pepper_from_file(pepper_filename)

    if choice == 'password':
        print("Enter the desired password length (12-50):")
        length = int(input().strip())
        password = generate_password(length)
        password_salt = hash_sha256(password + salt)
        password_salt_pepper = hash_sha256(password_salt + pepper)
        
        print(f"RAW Password: {password}")
        print(f"SHA-256 Encrypted: {hash_sha256(password)}")
        print(f"Salt: {salt}")
        print(f"Pass + Salt: {password_salt}")
        print(f"Pepper: {pepper}")
        print(f"Pass + Salt + Pepper: {password_salt_pepper}")

    elif choice == 'passphrase':
        print("Enter the desired number of words in the passphrase (3-10):")
        word_count = int(input().strip())
        passphrase = generate_passphrase(word_count)
        passphrase_salt = hash_sha256(passphrase + salt)
        passphrase_salt_pepper = hash_sha256(passphrase_salt + pepper)
        
        print(f"RAW Passphrase: {passphrase}")
        print(f"SHA-256 Encrypted: {hash_sha256(passphrase)}")
        print(f"Salt: {salt}")
        print(f"Passphrase + Salt: {passphrase_salt}")
        print(f"Pepper: {pepper}")
        print(f"Passphrase + Salt + Pepper: {passphrase_salt_pepper}")

    else:
        print("Invalid choice. Please enter 'password' or 'passphrase'.")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    print(f"Generated on: {timestamp}")

if __name__ == "__main__":
    main()
