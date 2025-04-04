from typing import Optional, Dict, Any


class QRCodeResponse:
    """
    Represents the response of a QR Code creation request.

    Attributes:
        id (str): The unique identifier of the QR Code.
        qr_code (str): The QR Code string.
        status (str): The current status of the QR Code.
        value (int): The value of the payment in cents.
        webhook_url (Optional[str]): The webhook URL for receiving notifications.
        qr_code_base64 (Optional[str]): The QR Code in Base64 format.
    """

    def __init__(
        self,
        id: str,
        qr_code: str,
        status: str,
        value: int,
        webhook_url: Optional[str],
        qr_code_base64: Optional[str],
    ) -> None:

        self.id = id
        self.qr_code = qr_code
        self.status = status
        self.value = value
        self.webhook_url = webhook_url
        self.qr_code_base64 = qr_code_base64

    def __str__(self) -> str:
        """
        Returns the string representation of the QRCodeResponse instance.

        Returns:
            str: The QR Code string.
        """
        return self.qr_code

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QRCodeResponse":
        """
        Creates an instance of QRCodeResponse from a dictionary.

        Args:
            data (Dict[str, Any]): The dictionary containing QR Code data.

        Returns:
            QRCodeResponse: An instance of QRCodeResponse.
        """
        return cls(
            id=data.get("id", ""),
            qr_code=data.get("qr_code", ""),
            status=data.get("status", ""),
            value=data.get("value", 0),
            webhook_url=data.get("webhook_url"),
            qr_code_base64=data.get("qr_code_base64"),
        )

    def update_status_from_dict(self, data: Dict[str, Any]) -> "QRCodeStatusResponse":
        """
        Updates the status of the QR Code from a dictionary.

        Args:
            data (Dict[str, Any]): The dictionary containing the updated status data.

        Returns:
            QRCodeStatusResponse: An instance of QRCodeStatusResponse with the updated status.
        """
        return QRCodeStatusResponse.from_dict(data)


class QRCodeStatusResponse:
    """
    Represents the status of a QR Code.

    Attributes:
        id (str): The unique identifier of the QR Code.
        status (str): The current status of the QR Code.
        value (int): The value of the payment in cents.
        description (Optional[str]): A description of the QR Code status.
        payment_type (Optional[str]): The type of payment.
        created_at (Optional[str]): The creation timestamp of the QR Code.
        updated_at (Optional[str]): The last update timestamp of the QR Code.
        webhook_url (Optional[str]): The webhook URL for receiving notifications.
        pix_details (Optional[Dict[str, Any]]): Additional details about the Pix transaction.
    """

    def __init__(
        self,
        id: str,
        status: str,
        value: int,
        description: Optional[str],
        payment_type: Optional[str],
        created_at: Optional[str],
        updated_at: Optional[str],
        webhook_url: Optional[str],
        pix_details: Optional[Dict[str, Any]],
    ) -> None:

        self.id = id
        self.status = status
        self.value = value
        self.description = description
        self.payment_type = payment_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.webhook_url = webhook_url
        self.pix_details = pix_details

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QRCodeStatusResponse":
        """
        Creates an instance of QRCodeStatusResponse from a dictionary.

        Args:
            data (Dict[str, Any]): The dictionary containing QR Code status data.

        Returns:
            QRCodeStatusResponse: An instance of QRCodeStatusResponse.
        """
        return cls(
            id=data.get("id", ""),
            status=data.get("status", ""),
            value=data.get("value", 0),
            description=data.get("description"),
            payment_type=data.get("payment_type"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            webhook_url=data.get("webhook_url"),
            pix_details=data.get("pix_details"),
        )
