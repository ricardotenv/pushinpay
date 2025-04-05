import requests
from typing import Optional, List, Dict, Any
from pushinpay.pix.responses.qrcode import QRCodeResponse, QRCodeStatusResponse

class Pix:
    """
    Pix is a class for interacting with the Pix-related endpoints of the PushinPay API.

    Attributes:
        _pushinpay (PushinPay): The main PushinPay client instance.
        _base_url (str): The base URL for Pix-related API requests.
        _headers (dict): The headers used for API requests.
    """

    def __init__(self, pushinpay: "PushinPay") -> None:
        from pushinpay import PushinPay
        self._pushinpay: PushinPay = pushinpay
        self._base_url: str = f"{pushinpay.base_url}/pix"
        self._headers: dict = pushinpay._headers()

    def create_qrcode(
        self, 
        value: int, 
        webhook_url: Optional[str] = None, 
        split_rules: Optional[List[Dict[str, Any]]] = None
    ) -> QRCodeResponse:
        """
        Creates a QR Code for Pix payment with optional split rules. -> https://doc.pushinpay.com.br/#criar-qrcode-pix

        Args:
            value (int): The value of the payment in cents.
            webhook_url (Optional[str]): The webhook URL for receiving notifications. Defaults to None.
            split_rules (Optional[List[Dict[str, Any]]]): A list of dictionaries defining split rules. 
                Each dictionary must contain:
                    - "value" (int): The value to split in cents.
                    - "account_id" (str): The account ID to receive the split.

        Returns:
            QRCodeResponse: An instance of QRCodeResponse containing the QR Code details.

        Raises:
            ValueError: If split_rules is not in the correct format.
            APIError: If the API returns an error.
        """
        if webhook_url is None:
            webhook_url = self._pushinpay.webhook_url

        # Validate split_rules
        if split_rules:
            if not isinstance(split_rules, list):
                raise ValueError("split_rules must be a list of dictionaries.")
            for rule in split_rules:
                if not isinstance(rule, dict) or "value" not in rule or "account_id" not in rule:
                    raise ValueError(
                        "Each split rule must be a dictionary with 'value' (int) and 'account_id' (str)."
                    )
                if not isinstance(rule["value"], int) or not isinstance(rule["account_id"], str):
                    raise ValueError("'value' must be an int and 'account_id' must be a str.")

        url = f"{self._base_url}/cashIn"
        payload = {"value": value}
        if webhook_url:
            payload["webhook_url"] = webhook_url
        if split_rules:
            payload["split_rules"] = split_rules

        response = requests.post(url, json=payload, headers=self._headers)
        self._handle_errors(response)
        return QRCodeResponse.from_dict(response.json())

    def get_status_qrcode(self, qrcode_response: QRCodeResponse) -> QRCodeStatusResponse:
        """
        Updates the status of a QR Code within the QRCodeResponse object. -> https://doc.pushinpay.com.br/#consultar-status-de-qrcode-pix
        This method retrieves the current status of a QR Code transaction using its ID and returns the updated status.

        Args:
            qrcode_response (QRCodeResponse): The QRCodeResponse object to update.

        Returns:
            QRCodeStatusResponse: An instance of QRCodeStatusResponse containing the updated status.
        """
        url = f"{self._pushinpay.base_url}/transactions/{qrcode_response.id}"
        response = requests.get(url, headers=self._headers)
        self._handle_errors(response)
        status = qrcode_response.update_status_from_dict(response.json())
        return status

    def _handle_errors(self, response: requests.Response) -> None:
        """
        Checks and raises errors from the API response.

        Args:
            response (requests.Response): The response object from the API request.

        Raises:
            Exception: If the API response indicates an error.
        """
        if not response.ok:
            raise Exception(f"API Error: {response.status_code} - {response.text}")