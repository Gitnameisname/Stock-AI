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