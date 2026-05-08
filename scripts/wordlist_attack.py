import hashlib

# Read target hash
with open("hashes/sample_hash.txt", "r") as file:
    target_hash = file.read().strip()

# Read wordlist
with open("wordlists/common_passwords.txt", "r") as file:
    passwords = file.readlines()

print("\nStarting Wordlist Attack...\n")

# Try each password
for password in passwords:

    # Remove spaces/newlines
    password = password.strip()

    # Convert password into MD5 hash
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    print(f"Trying: {password}")

    # Compare hashes
    if hashed_password == target_hash:
        print("\nPASSWORD FOUND!")
        print(f"Password: {password}")
        break

else:
    print("\nPassword not found in wordlist.")