import hashlib
# from app.settings import SECRET_KEY_FERNET

"""
Fernet.generate_key()
b'QaBguu2w72LwQxHTg5KWa77gVeez5d_MGm2v5KN9ucI='
"""
# SECRET_KEY_FERNET = b'QaBguu2w72LwQxHTg5KWa77gVeez5d_MGm2v5KN9ucI='

def encrypt_people_id(people_id):
    hashed_people_id = hashlib.sha256(people_id.encode()).hexdigest()
    return hashed_people_id
# def encrypt_people_id(people_id):
#     print("SECRET_KEY_FERNET", SECRET_KEY_FERNET)
#     cipher_suite = Fernet(SECRET_KEY_FERNET)
#     encrypted_people_id = cipher_suite.encrypt(people_id.encode())
#     return encrypted_people_id.decode()

# def decrypt_people_id(encrypted_people_id):
#     cipher_suite = Fernet(SECRET_KEY_FERNET)
#     decrypted_people_id = cipher_suite.decrypt(encrypted_people_id).decode()
#     return decrypted_people_id


if __name__ == "__main__":
    # Example usage
    people_ids = ["manh-nx", "ha-pn", "duc-nx", "huong-th"]
    for people_id in people_ids:
        encrypted_id = encrypt_people_id(people_id)
        print(people_id, encrypted_id)

    # decrypted_id = decrypt_people_id(encrypted_id)
    # print("Decrypted:", decrypted_id)
