import json
from encryptor import encrypt
from decryptor import decrypt_data

plaintext = json.dumps({"message": "Hello World"}).encode()

ciphertext, tag, nonce, cipher_text_blob = encrypt(plaintext)

print(ciphertext)

result = decrypt_data(ciphertext, tag, nonce, cipher_text_blob)

response = json.loads(result)
print(response["message"])