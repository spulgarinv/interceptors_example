import boto3
import base64
from Crypto.Cipher import AES

def encrypt(message: str):
    client = boto3.client(
        "kms",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1"
    )
    
    data_key = client.generate_data_key(
        KeyId="",
        KeySpec='AES_128'
    )
    
    cipher_text_blob = data_key.get('CiphertextBlob')
    plaintext_key = data_key.get('Plaintext')
    
    cypher = AES.new(plaintext_key, AES.MODE_OCB)
    
    ciphertext, tag = cypher.encrypt_and_digest(message)
    
    return ciphertext, tag, cypher.nonce, cipher_text_blob