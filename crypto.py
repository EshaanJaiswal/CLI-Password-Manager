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
        except FileNotFoundError:
            key = os.urandom(32)
            with open(KEY_FILE, 'wb') as f:
                f.write(base64.urlsafe_b64encode(key))
            return key
        else:
            return base64.urlsafe_b64decode(data)
    
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
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(data))
    