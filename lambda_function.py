import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        if isinstance(event, str):
            event = json.loads(event)
        
        numero = event.get("numero")
        mensagem = event.get("mensagem", "Olá! Esta é uma mensagem enviada via AWS Lambda.")

        if not numero:
            return {
                "statusCode": 400,
                "body": json.dumps({"erro": "Número de telefone não fornecido."})
            }
        
        response = sns.publish(
            PhoneNumber=numero,
            Message=mensagem
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "mensagem": "Mensagem enviada com sucesso!",
                "response": response
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": str(e)})
        }
