from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import base64
import hashlib

def decrypt(encrypted_text, passphrase):
    try:
        # Decode the base64 encoded string
        encrypted_data = base64.b64decode(encrypted_text)
        
        # Extract the salt (first 8 bytes)
        salt = encrypted_data[:8]
        
        # Derive the key and IV using PBKDF2 with SHA256
        key_iv = PBKDF2(passphrase, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)
        key = key_iv[:16]
        iv = key_iv[16:]
        
        # Create the AES cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt the data (excluding the salt)
        decrypted_data = cipher.decrypt(encrypted_data[8:])
        
        # Remove padding
        padding_length = decrypted_data[-1]
        if padding_length > AES.block_size or padding_length < 1:
            raise ValueError("Invalid padding length")
        
        # Verify padding
        if decrypted_data[-padding_length:] != bytes([padding_length]) * padding_length:
            raise ValueError("Invalid padding")
        
        decrypted_data = decrypted_data[:-padding_length]
        
        return decrypted_data.decode('utf-8')
    
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None

# Example usage
encrypted_text = "U2FsdGVkX19JRQkszZe00Igg/M0qRQ3LdxkZNZCi9j/ZagF0/P/EhKNDhOlpprwN"
passphrase = "f0cfe28f452b480cbcbaf50af2ca1a70"
decrypted_text = decrypt(encrypted_text, passphrase)
if decrypted_text:
    print(decrypted_text)