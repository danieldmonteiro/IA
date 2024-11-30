# Usar a API de conversação para enviar a mensagem - Amazon Titan Text

import boto3
from botocore.exceptions import ClientError

# Criar o Bedrock Runtime client na região AWS de uso
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Setar ID do modelo, exemplo: Titan Text Premier
model_id = "amazon.titan-text-premier-v1:0"

# Startar o dialogo com o emissor da mensagem
user_message = "Qual foi o primeiro europeu a chegar no continente americano?"
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Enviar a mensagem para o modelo, usando a inferência do modelo
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extrair e printar a resposta
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERRO: Falha na chamada '{model_id}'. Erro: {e}")
    exit(1)