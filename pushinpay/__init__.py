from typing import Optional, Dict
from pushinpay.pix import Pix

class PushinPay:
    """
    PushinPay is the main class for interacting with the PushinPay API.

    Attributes:
        api_key (str): The API key used for authentication -> https://doc.pushinpay.com.br/#autenticacao
        webhook_url (Optional[str]): The default webhook URL for receiving notifications.
        sandbox (bool): Whether to use the sandbox environment.
    """

    def __init__(self, api_key: str, webhook_url: Optional[str] = None, sandbox: bool = False) -> None:
        self._base_url: str = (
            "https://api-sandbox.pushinpay.com.br/api" if sandbox else "https://api.pushinpay.com.br/api"
        )
        self.api_key: str = api_key
        self.webhook_url: Optional[str] = webhook_url
        self._pix: Pix = Pix(self)

    @property
    def base_url(self) -> str:
        """
        Returns the base URL of the API.

        Returns:
            str: The base URL of the API.
        """
        return self._base_url

    @property
    def pix(self) -> Pix:
        """
        Provides access to the Pix API.

        Returns:
            Pix: An instance of the Pix class for interacting with Pix-related endpoints.
        """
        return self._pix

    def _headers(self) -> Dict[str, str]:
        """
        Generates the headers required for API requests.

        Returns:
            Dict[str, str]: A dictionary containing the headers for API requests.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }