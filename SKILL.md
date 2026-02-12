---
name: doordash
description: Interact with DoorDash Drive API for delivery management.
---

# DoorDash Skill

This skill provides integration with the DoorDash Drive API for delivery management.

## Setup

1.  **Retrieve API Keys:** Log in to [DoorDash Developer Portal](https://developer.doordash.com/portal/login) and get your:
    - Developer ID
    - Key ID
    - Signing Secret

2.  **Configure Authentication:**
    - Open `skills/doordash/scripts/auth.py`.
    - Replace the placeholder values for `DEVELOPER_ID`, `KEY_ID`, and `SIGNING_SECRET`.
    - Alternatively, set them as environment variables: `DD_DEVELOPER_ID`, `DD_KEY_ID`, `DD_SIGNING_SECRET`.

## Usage

### Create a Delivery
Run the script with a JSON payload file:
```bash
python3 skills/doordash/scripts/create_delivery.py path/to/payload.json
```

### Check Delivery Status
Run the script with the delivery ID:
```bash
python3 skills/doordash/scripts/get_delivery_status.py <delivery_id>
```

## References

- `references/api.md`: API schema and endpoint details.
