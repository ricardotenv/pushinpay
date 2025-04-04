from typing import Optional


class PushinPayError(Exception):
    """
    Base exception for errors in the PushinPay library.
    """
    pass


class APIError(PushinPayError):
    """
    Exception for errors related to the PushinPay API.

    Attributes:
        status_code (int): The HTTP status code returned by the API.
        message (str): The error message returned by the API.
    """

    def __init__(self, status_code: int, message: Optional[str]) -> None:
        """
        Initializes an APIError instance.

        Args:
            status_code (int): The HTTP status code returned by the API.
            message (Optional[str]): The error message returned by the API.
        """
        self.status_code: int = status_code
        self.message: Optional[str] = message
        super().__init__(f"APIError {status_code}: {message}")
