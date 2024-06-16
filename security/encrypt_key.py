import os
from cryptography.fernet import Fernet

def generate_key():
    """
    English:
    Generates a key and saves it into a file.

    Korean:
    키를 생성하고 파일에 저장합니다.
    """
    key = Fernet.generate_key()
    with open("security/secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    English:
    Loads the key from the current directory named `secret.key`.

    Korean:
    `secret.key`라는 이름의 파일에서 키를 로드합니다.
    """
    return open("security/secret.key", "rb").read()

def encrypt_api_key(api_key: str) -> bytes:
    """
    English:
    Encrypts the API key.

    Korean:
    API 키를 암호화합니다.
    """
    key = load_key()
    f = Fernet(key)
    encrypted_key = f.encrypt(api_key.encode())
    return encrypted_key

def main():
    # Generate key if it doesn't exist
    # 키가 존재하지 않으면 생성
    if not os.path.exists("security/secret.key"):
        generate_key()

    # Read the API key from api.txt
    # api.txt에서 API 키를 읽어옵니다.
    with open("security/api.txt", "r") as file:
        api_key = file.read().strip()

    # Encrypt the API key
    # API 키를 암호화합니다.
    encrypted_key = encrypt_api_key(api_key)

    # Write the encrypted API key to api_encrypted.txt
    # 암호화된 API 키를 api_encrypted.txt에 저장합니다.
    with open("security/api_encrypted.txt", "wb") as file:
        file.write(encrypted_key)

    # Delete the original api.txt file
    # 원래의 api.txt 파일을 삭제합니다.
    os.remove("security/api.txt")
    print("API key encrypted and saved to api_encrypted.txt. Original api.txt file deleted.")

if __name__ == "__main__":
    main()
