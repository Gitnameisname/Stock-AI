from cryptography.fernet import Fernet

def load_key():
    """
    English:
    Loads the key from the current directory named `secret.key`.

    Korean:
    `secret.key`라는 이름의 파일에서 키를 로드합니다.
    """
    return open("security/secret.key", "rb").read()

def decrypt_api_key(encrypted_key: bytes) -> str:
    """
    English:
    Decrypts the API key.

    Korean:
    API 키를 복호화합니다.
    """
    key = load_key()
    f = Fernet(key)
    decrypted_key = f.decrypt(encrypted_key).decode()
    return decrypted_key

def main():
    # Read the encrypted API key from api_encrypted.txt
    # api_encrypted.txt에서 암호화된 API 키를 읽어옵니다.
    with open("security/api_encrypted.txt", "rb") as file:
        encrypted_key = file.read()

    # Decrypt the API key
    # API 키를 복호화합니다.
    api_key = decrypt_api_key(encrypted_key)
    print("Decrypted API key:", api_key)

if __name__ == "__main__":
    main()
