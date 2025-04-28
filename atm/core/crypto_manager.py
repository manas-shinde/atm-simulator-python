from cryptography.fernet import Fernet
import json
import os


class CryptoManager:
    def __init__(self, key_file='key.key'):
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                self.key = f.read()
        else:
            self.key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(self.key)

        self.cipher = Fernet(self.key)

    def encrypt_data(self, data: dict) -> bytes:
        json_data = json.dumps(data)
        encrypted = self.cipher.encrypt(json_data.encode())
        return encrypted

    def decrypt_data(self, encrypted_data: bytes) -> dict:
        decrypted = self.cipher.decrypt(encrypted_data)
        json_data = decrypted.decode()
        return json.loads(json_data)

    def save_to_file(self, filename: str, data: dict):
        base_dir = os.path.dirname(__file__)  # 📍 This gets the current file's folder (like atm/utils/)
        data_dir = os.path.join(base_dir, '..', 'data')  # 📍 Go one up to atm/, then inside data/
        os.makedirs(data_dir, exist_ok=True)

        file_path = os.path.join(data_dir, filename)
        if not os.path.exists(file_path):
            file = open(file_path, 'w')
            file.close()
        encrypted_data = self.encrypt_data(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)

    def load_from_file(self, filename: str):
        base_dir = os.path.dirname(__file__)  # 📍 Current folder
        data_dir = os.path.join(base_dir, '..')  # 📍 atm/data/
        file_path = os.path.join(data_dir, filename)

        if not os.path.exists(file_path):
            print(f"⚠️ File {file_path} not found. Returning empty data.")
            return {}

        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = self.decrypt_data(encrypted_data)
        return decrypted_data
