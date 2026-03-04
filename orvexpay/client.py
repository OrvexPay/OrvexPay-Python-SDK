from typing import Any, Dict, Optional
import httpx
from .exceptions import OrvexApiError

class OrvexClient:
    """Official OrvexPay API Client."""

    def __init__(
        self, 
        api_key: str, 
        base_url: str = "https://api.orvexpay.com",
        timeout: float = 30.0
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.timeout = timeout

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        if response.is_success:
            return response.json()
        
        try:
            data = response.json()
            message = data.get("message", response.text)
        except Exception:
            data = None
            message = response.text

        raise OrvexApiError(
            message=f"OrvexPay API Error: {message}",
            status_code=response.status_code,
            response_data=data
        )

    # Synchronous Methods
    def create_invoice(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Creates a new payment invoice."""
        with httpx.Client(base_url=self.base_url, headers=self.headers, timeout=self.timeout) as client:
            response = client.post("/api/invoice", json=params)
            return self._handle_response(response)

    def get_invoice(self, invoice_id: str) -> Dict[str, Any]:
        """Retrieves details of an existing invoice."""
        with httpx.Client(base_url=self.base_url, headers=self.headers, timeout=self.timeout) as client:
            response = client.get(f"/api/invoice/{invoice_id}")
            return self._handle_response(response)

    # Asynchronous Methods
    async def create_invoice_async(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Creates a new payment invoice asynchronously."""
        async with httpx.AsyncClient(base_url=self.base_url, headers=self.headers, timeout=self.timeout) as client:
            response = await client.post("/api/invoice", json=params)
            return self._handle_response(response)

    async def get_invoice_async(self, invoice_id: str) -> Dict[str, Any]:
        """Retrieves details of an existing invoice asynchronously."""
        async with httpx.AsyncClient(base_url=self.base_url, headers=self.headers, timeout=self.timeout) as client:
            response = await client.get(f"/api/invoice/{invoice_id}")
            return self._handle_response(response)
