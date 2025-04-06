# PushinPay

pushinpay é uma biblioteca Python para integração com a API do gateway de pagamento [PushinPay](https://pushinpay.com.br/), permitindo a criação e gerenciamento de pagamentos via Pix.

Documentação oficial: https://doc.pushinpay.com.br/#introducao

## Instalação

Para instalar a biblioteca, utilize o `pip`:

```bash
pip install pushinpay
```

## Configuração

Para começar a usar a biblioteca, você precisa de uma chave de API fornecida pelo PushinPay. Você pode configurar a biblioteca da seguinte forma:

```python
from pushinpay import PushinPay

# Inicialize o cliente PushinPay
pushinpay = PushinPay(api_key="SUA_CHAVE_API", webhook_url="https://seu-webhook.com", sandbox=True)
```

- `api_key`: Sua chave de API.
- `webhook_url`: (Opcional) URL para receber notificações de eventos.
- `sandbox`: (Opcional) Define se o ambiente de sandbox será utilizado. O padrão é `False`.

## Funcionalidades

### Criar QR Code Pix

Você pode criar um QR Code Pix para pagamentos:

```python
# Criar um QR Code Pix
qrcode = pushinpay.pix.create_qrcode(value=1000)  # Valor em centavos (R$10,00)
print(qrcode)  # Código "copia e cola" do QR Code
# Ou
print(qrcode.qr_code) # Código "copia e cola" do QR Code
```

### Criar um QR Code Pix com regras de divisão (split)

```python
split_rules = [
    {"value": 500, "account_id": "9C3AD98C-F00B-4729-BEAC-0A4B70B3A043"},
    {"value": 1500, "account_id": "1A2B3C4D-5678-90EF-1234-567890ABCDEF"} 
]

qrcode = pushinpay.pix.create_qrcode(
    value=2000, # Valor total em centavos (R$20,00)
    webhook_url="http://meu-webhook.com",
    split_rules=split_rules
)

print(qrcode) # Código "copia e cola" do QR Code
```

### Consultar Status de um QR Code Pix

Para consultar o status de um QR Code Pix:

```python
qrcode_status = pushinpay.pix.get_status_qrcode(qrcode.id)  # Passar o ID do QR Code
print(qrcode_status)  # A representação em texto do atributo status
print(qrcode_status.value)  # Valor do pagamento em centavos
```

## Tratamento de Erros

A biblioteca lança exceções específicas para erros da API:

- `PushinPayError`: Exceção base para erros da biblioteca.
- `APIError`: Exceção para erros retornados pela API.

Exemplo de tratamento de erros:

```python
from pushinpay.errors import APIError

try:
    qrcode = pushinpay.pix.create_qrcode(value=1000)
except APIError as e:
    print(f"Erro na API: {e.status_code} - {e.message}")
```

## Requisitos

- Python 3.6 ou superior
- Biblioteca `requests`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.

## Testes

Para executar os testes da biblioteca, utilize o seguinte comando:

```bash
python -m unittest discover tests
```

Certifique-se de que o módulo `unittest` está configurado corretamente no seu ambiente.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
