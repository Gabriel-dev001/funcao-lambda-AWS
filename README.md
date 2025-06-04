# Função AWS Lambda - Envio de SMS com Amazon SNS

Esta função permite enviar mensagens de texto (SMS) usando o serviço Amazon SNS diretamente de uma função Lambda em Python.

---

# Link da Lambda:
https://sa-east-1.console.aws.amazon.com/lambda/home?region=sa-east-1#/functions/enviarSMS?newFunction=true&tab=code

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
