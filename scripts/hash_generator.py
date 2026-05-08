import hashlib

# Take password input
password = input("Enter a password: ")

# Convert password into bytes
encoded_password = password.encode()

# Generate MD5 hash
md5_hash = hashlib.md5(encoded_password).hexdigest()

# Generate SHA1 hash
sha1_hash = hashlib.sha1(encoded_password).hexdigest()

# Generate SHA256 hash
sha256_hash = hashlib.sha256(encoded_password).hexdigest()

# Display hashes
print("\nGenerated Hashes:")
print("-" * 50)

print(f"MD5    : {md5_hash}")
print(f"SHA1   : {sha1_hash}")
print(f"SHA256 : {sha256_hash}")