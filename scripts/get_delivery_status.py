import json
import urllib.request
import urllib.error
import sys
import os

# Ensure we can import auth.py from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
from auth import get_token

API_URL_BASE = "https://openapi.doordash.com/drive/v2/deliveries"

def get_delivery_status(delivery_id):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    url = f"{API_URL_BASE}/{delivery_id}"
    req = urllib.request.Request(url, headers=headers)
    
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
        print("Usage: python3 get_delivery_status.py <delivery_id>")
        sys.exit(1)
        
    delivery_id = sys.argv[1]
    get_delivery_status(delivery_id)
