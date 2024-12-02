import boto3
from botocore.exceptions import ClientError
import sys
import os

# Adicionar o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar o módulo da função fibonacci
from exercicio_5.exercicio4 import fibonacci

sequenciaTeste = fibonacci()


# Criar o client Bedrock Runtime na região AWS de uso
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Setar o ID do modelo, exemplo: Titan Text Premier
model_id = "amazon.titan-text-premier-v1:0"

# Solicita ao usuário que insira sua mensagem
user_message = f"Qual o nome dessa sequência numérica  {sequenciaTeste}? Conte a sua história"

# Startar a conversação: mensagem
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Envia a mensagem para o modelo, usando a inferência
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extrair e printar a resposta
    response_text = response["output"]["message"]["content"][0]["text"]
    print("\nResposta do modelo:\n")
    print(response_text)
    print()

except (ClientError, Exception) as e:
    print(f"\nERRO: Falha na chamada '{model_id}'. Erro: {e}\n")
    exit(1)