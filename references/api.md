# DoorDash Drive API Reference

## Authentication

Authentication is performed using a JSON Web Token (JWT) signed with HS256.
The JWT must include the following claims:
- `aud`: "doordash"
- `iss`: Developer ID
- `kid`: Key ID
- `exp`: Expiration time (unix timestamp)
- `iat`: Issued at time (unix timestamp)

## Endpoints

### Create Delivery

**Endpoint:** `POST /drive/v2/deliveries`

**Request Body (JSON):**

```json
{
  "external_delivery_id": "unique_id_123",
  "pickup_address": "123 Main St, San Francisco, CA 94105",
  "pickup_business_name": "Example Restaurant",
  "pickup_phone_number": "+16505555555",
  "dropoff_address": "456 Market St, San Francisco, CA 94105",
  "dropoff_business_name": "Customer Name",
  "dropoff_phone_number": "+16505555556",
  "order_value": 2000,
  "currency": "USD"
}
```

**Response (JSON):**

```json
{
  "delivery_id": "D-12345",
  "status": "created",
  ...
}
```

### Get Delivery Status

**Endpoint:** `GET /drive/v2/deliveries/{delivery_id}`

**Response (JSON):**

```json
{
  "delivery_id": "D-12345",
  "status": "dasher_confirmed",
  "dasher_status": "en_route_to_pickup",
  ...
}
```

## Useful Links

- [DoorDash Drive API Documentation](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started)
