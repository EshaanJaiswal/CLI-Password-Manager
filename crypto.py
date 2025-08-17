import os
import base64
try:
    from .constants import KEY_FILE
except ImportError:
    from constants import KEY_FILE

class Crypto:
    def __init__(self):
        self.key = self.load_or_generate_key()
    
    def load_or_generate_key(self):
        try:
            with open(KEY_FILE, 'rb') as f:
                data = f.read()
                if not data:  # File exists but is empty
                    raise ValueError("Empty key file")
                decoded_key = base64.urlsafe_b64decode(data)
                if len(decoded_key) == 0:  # Decoded key is empty
                    raise ValueError("Empty decoded key")
                return decoded_key
        except (FileNotFoundError, ValueError, Exception):
            # Generate new key if file doesn't exist, is empty, or corrupted
            key = os.urandom(32)
            with open(KEY_FILE, 'wb') as f:
                f.write(base64.urlsafe_b64encode(key))
            return key
    
    def encrypt(self, plaintext: str) -> str:
        raw = plaintext.encode('utf-8')
        cypher = self.xor_bytes(raw)
        return base64.urlsafe_b64encode(cypher).decode('ascii')
    
    def decrypt(self, token: str) -> str:
        cypher = base64.urlsafe_b64decode(token.encode('ascii'))
        raw = self.xor_bytes(cypher)
        return raw.decode('utf-8')
    
    def xor_bytes(self, data: bytes) -> bytes:
        k = self.key
        if len(k) == 0:
            raise ValueError("Encryption key is empty")
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(data))
    