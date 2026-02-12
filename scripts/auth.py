import json
import time
import uuid
import hmac
import hashlib
import base64
import os

def create_jwt(developer_id, key_id, signing_secret):
    """
    Generates a JWT for DoorDash Drive API authentication using HS256.
    """
    header = {
        "alg": "HS256",
        "typ": "JWT",
        "dd-ver": "DD-JWT-V1"
    }
    
    payload = {
        "aud": "doordash",
        "iss": developer_id,
        "kid": key_id,
        "exp": int(time.time() + 300),  # 5 minutes expiry
        "iat": int(time.time()),
        "jti": str(uuid.uuid4())
    }
    
    # Base64url encode header and payload
    def base64url_encode(data):
        return base64.urlsafe_b64encode(json.dumps(data).encode('utf-8')).decode('utf-8').rstrip('=')
    
    encoded_header = base64url_encode(header)
    encoded_payload = base64url_encode(payload)
    
    # Create signature
    try:
        # Decode the signing secret (it's base64url encoded by DoorDash)
        secret_bytes = base64.urlsafe_b64decode(signing_secret + '=' * (-len(signing_secret) % 4))
    except Exception:
        # Fallback for standard base64 or raw string if needed (though unlikely for DD)
        secret_bytes = signing_secret.encode('utf-8')

    signature_input = f"{encoded_header}.{encoded_payload}"
    signature = hmac.new(
        secret_bytes,
        signature_input.encode('utf-8'),
        hashlib.sha256
    ).digest()
    
    encoded_signature = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
    
    return f"{encoded_header}.{encoded_payload}.{encoded_signature}"

# Placeholder credentials - REPLACE THESE
DEVELOPER_ID = os.getenv("DD_DEVELOPER_ID", "REPLACE_WITH_DEVELOPER_ID")
KEY_ID = os.getenv("DD_KEY_ID", "REPLACE_WITH_KEY_ID")
SIGNING_SECRET = os.getenv("DD_SIGNING_SECRET", "REPLACE_WITH_SIGNING_SECRET")

def get_token():
    if "REPLACE_WITH" in [DEVELOPER_ID, KEY_ID, SIGNING_SECRET]:
        raise ValueError("DoorDash credentials not set. Please set DD_DEVELOPER_ID, DD_KEY_ID, and DD_SIGNING_SECRET environment variables or update auth.py.")
    return create_jwt(DEVELOPER_ID, KEY_ID, SIGNING_SECRET)
