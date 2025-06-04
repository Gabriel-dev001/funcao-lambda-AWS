# Função AWS Lambda - Envio de SMS com Amazon SNS

Esta função permite enviar mensagens de texto (SMS) usando o serviço Amazon SNS diretamente de uma função Lambda em Python.

---

# Link da Lambda:

https://ebugzynjhbc24353ofcakkfiyu0rjdof.lambda-url.sa-east-1.on.aws/

---

# Objetivo

Demonstrar o uso do serviço Amazon SNS integrado a uma função Lambda para envio de mensagens SMS.

---

# Linguagem e Configurações

- **Linguagem:** Python 3.13  
- **Serviço AWS:** Lambda + SNS  
- **Dependência:** boto3 (já disponível no ambiente padrão da AWS Lambda)

---

# Como funciona

### Entrada esperada

```json
{
  "numero": "+55S44999309823",
  "mensagem": "Sua mensagem personalizada aqui."
}
```

### Entrada esperada

```json
{
  "mensagem": "Mensagem enviada com sucesso!",
  "response": {
  }
}
