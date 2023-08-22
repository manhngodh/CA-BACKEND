from cryptography.fernet import Fernet

# Generate a secret key for encryption (keep this secure!)
SECRET_KEY = b'SomeSuperSecretKey123'

def encrypt_people_id(people_id):
    cipher_suite = Fernet(SECRET_KEY)
    encrypted_people_id = cipher_suite.encrypt(people_id.encode())
    return encrypted_people_id

def decrypt_people_id(encrypted_people_id):
    cipher_suite = Fernet(SECRET_KEY)
    decrypted_people_id = cipher_suite.decrypt(encrypted_people_id).decode()
    return decrypted_people_id

# Example usage
people_id = "12345"
encrypted_id = encrypt_people_id(people_id)
print("Encrypted:", encrypted_id)

decrypted_id = decrypt_people_id(encrypted_id)
print("Decrypted:", decrypted_id)
