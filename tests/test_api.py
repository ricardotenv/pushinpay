import unittest
from unittest.mock import patch, MagicMock
from pushinpay import PushinPay
from pushinpay.pix.responses.qrcode import QRCodeResponse, QRCodeStatusResponse

class TestPixAPI(unittest.TestCase):
    def setUp(self):
        self.pushinpay = PushinPay(api_key="test_api_key", webhook_url="http://teste.com", sandbox=True)

    @patch("requests.post")
    def test_create_qrcode(self, mock_post):
        # Mock response for create_qrcode
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "id": "9c29870c-9f69-4bb6-90d3-2dce9453bb45",
            "qr_code": "00020101021226770014BR.GOV.BCB.PIX2555api...",
            "status": "created",
            "value": 35,
            "webhook_url": "http://teste.com",
            "qr_code_base64": "data:image/png;base64,iVBORw0KGgoAA....."
        }
        mock_post.return_value = mock_response

        # Call create_qrcode
        qrcode = self.pushinpay.pix.create_qrcode(value=35)

        # Assertions
        self.assertIsInstance(qrcode, QRCodeResponse)
        self.assertEqual(qrcode.id, "9c29870c-9f69-4bb6-90d3-2dce9453bb45")
        self.assertEqual(qrcode.status, "created")
        self.assertEqual(qrcode.value, 35)
        self.assertEqual(qrcode.webhook_url, "http://teste.com")

    @patch("requests.get")
    def test_get_status_qrcode(self, mock_get):
        # Mock response for get_status_qrcode
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "id": "9C17B975-903F-44CB-BB70-E838F85DC228",
            "status": "created",
            "value": 72,
            "description": None,
            "payment_type": "pix",
            "created_at": "2024-05-21T02:04:56.703000Z",
            "updated_at": "2024-05-21T02:04:56.703000Z",
            "webhook_url": "https://seu-tite.com",
            "pix_details": {
                "id": "9C17B975-8F08-445D-9BBB-C40572C1E446",
                "expiration_date": "2024-05-21 02:09:56.000",
                "emv": "00020101021226770014BR.GOV.BCB.PIX2555api.itau/pix/qr/v2/01dd8aba-a56c-4623-aa90-3ade0aea1ebe5204000053039865802BR5910PUSHIN PAY6009SAO PAULO62070503***63047D83",
                "created_at": "2024-05-21T02:04:56.703000Z",
                "updated_at": "2024-05-21T02:04:56.703000Z"
            }
        }
        mock_get.return_value = mock_response

        # Call get_status_qrcode
        qrcode_status = self.pushinpay.pix.get_status_qrcode("9C17B975-903F-44CB-BB70-E838F85DC228")

        # Assertions
        self.assertIsInstance(qrcode_status, QRCodeStatusResponse)
        self.assertEqual(qrcode_status.id, "9C17B975-903F-44CB-BB70-E838F85DC228")
        self.assertEqual(qrcode_status.status, "created")
        self.assertEqual(qrcode_status.value, 72)
        self.assertEqual(qrcode_status.webhook_url, "https://seu-tite.com")

if __name__ == "__main__":
    unittest.main()
