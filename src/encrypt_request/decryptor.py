import boto3
from Crypto.Cipher import AES
import sys

def decrypt_data(ciphertext, tag, nonce, cipher_text_blob):
    kms_client = boto3.client(
        'kms',
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1"
    )
    
    decrypted_key = kms_client.decrypt(CiphertextBlob=cipher_text_blob).get('Plaintext')
    cipher = AES.new(decrypted_key, AES.MODE_OCB, nonce=nonce)
    try:
        message = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        print("The message was modified!")
        sys.exit(1)
    
    return message