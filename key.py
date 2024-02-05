import secrets

# Generate a random 32-byte (256-bit) secret key
secret_key = secrets.token_hex(32)

print(f"Your secret key: {secret_key}")
