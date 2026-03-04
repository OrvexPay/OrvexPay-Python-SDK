# OrvexPay Python SDK

Official Python SDK for the OrvexPay Payment Gateway.

## Installation

Install via pip:

```bash
pip install orvexpay
```

## Usage

### Synchronous Usage

```python
from orvexpay import OrvexClient

client = OrvexClient(api_key="your-api-key")

# Create an invoice
invoice = client.create_invoice({
    "priceAmount": "100.00",
    "priceCurrency": "USD",
    "payCurrency": "USDT",
    "orderId": "ORDER-12345",
    "successUrl": "https://example.com/success",
    "cancelUrl": "https://example.com/cancel"
})

print(f"Invoice ID: {invoice['id']}")
print(f"Pay URL: {invoice['payUrl']}")
```

### Asynchronous Usage

```python
import asyncio
from orvexpay import OrvexClient

async def main():
    client = OrvexClient(api_key="your-api-key")
    
    invoice = await client.create_invoice_async({
        "priceAmount": "100.00",
        "priceCurrency": "USD",
        "payCurrency": "USDT"
    })
    
    print(f"Async Invoice ID: {invoice['id']}")

asyncio.run(main())
```

## Features

- **Sync & Async**: Built-in support for both synchronous and asynchronous workflows using `httpx`.
- **Type Safety**: Fully type-hinted for better IDE support.
- **Easy Integration**: Simple DTO pattern for API requests.
- **Error Handling**: Detailed exceptions for API and network errors.
