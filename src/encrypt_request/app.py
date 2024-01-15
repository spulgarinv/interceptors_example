import json
import base64
from fastapi import FastAPI
from functools import wraps

from encryptor import encrypt

def interceptor(func):
    print("This is executed at function definition time (def my_func)")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("This is executed before function call")
        result = func(*args, **kwargs)
        print("This is executed after function call")
        ciphertext, tag, nonce, cipher_text_blob  = encrypt(json.dumps(result).encode())
        
        return {
            "tag": base64.b64encode(tag).decode(),
            "nonce": base64.b64encode(nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "cipher_text_blob": base64.b64encode(cipher_text_blob).decode()
        }    
    return wrapper

app = FastAPI()

@app.post("/say-hi")
@interceptor
def handle_hello():
    return {
        "message": "hi"
    }