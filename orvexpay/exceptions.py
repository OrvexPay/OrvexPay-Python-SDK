from typing import Any, Dict, Optional

class OrvexError(Exception):
    """Base exception for all OrvexPay errors."""
    pass

class OrvexApiError(OrvexError):
    """Exception raised for errors returned by the OrvexPay API."""
    def __init__(self, message: str, status_code: int, response_data: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data
