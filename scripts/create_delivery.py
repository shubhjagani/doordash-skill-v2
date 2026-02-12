import json
import urllib.request
import urllib.error
import sys
import os

# Ensure we can import auth.py from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
from auth import get_token

API_URL = "https://openapi.doordash.com/drive/v2/deliveries"

def create_delivery(payload):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(API_URL, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                result = json.loads(response.read().decode('utf-8'))
                print(json.dumps(result, indent=2))
                return result
            else:
                print(f"Error: {response.status} - {response.read().decode('utf-8')}")
                return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 create_delivery.py <payload.json>")
        sys.exit(1)
        
    payload_file = sys.argv[1]
    if not os.path.exists(payload_file):
        print(f"Error: File '{payload_file}' not found.")
        sys.exit(1)
        
    with open(payload_file, 'r') as f:
        payload = json.load(f)
        
    create_delivery(payload)
