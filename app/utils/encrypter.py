from cryptography.fernet import Fernet
from app.config.enviroments import get_environment_variables

ENV = get_environment_variables()
FERNET = Fernet(ENV.ENCRYPT_HASH)

class Encrypter:
    def __init__(self) -> None:
        pass
    
    def encrypt(self, text_to_encrypt: str) -> str:
        encrypted_text = FERNET.encrypt(text_to_encrypt.encode('utf-8')).decode()
        return encrypted_text

    def validate_encrypted_text(self, plain_text: str, encrypted_text: str) -> bool:
        try:
            decrypted_text = FERNET.decrypt(encrypted_text.encode()).decode('utf-8')
            return decrypted_text == plain_text
        except Exception as e:
            return False
