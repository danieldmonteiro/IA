# Usar a API de conversação para enviar uma mensagem de texto para o Amazon Titan Text

import boto3
from botocore.exceptions import ClientError

# Criar o client Bedrock Runtime na região AWS de uso
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Setar o ID do modelo, exemplo: Titan Text Premier
model_id = "amazon.titan-text-premier-v1:0"

# Solicita ao usuário que insira sua mensagem
user_message = input(
    "Bem-vindo ao Assistente Virtual! Sou um assistente de IA aqui para ajudar com suas dúvidas, "
    "oferecer informações ou realizar tarefas específicas.\n"
    "Você pode perguntar sobre:\n"
    "- Informações gerais: fatos, notícias, explicações.\n"
    "- Tarefas práticas: criar textos, planejar algo, resolver cálculos.\n"
    "- Entretenimento: piadas, histórias ou ideias criativas.\n"
    "\nComo posso ajudar você hoje? "
)

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
    print("\nResposta do modelo:")
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERRO: Falha na chamada '{model_id}'. Erro: {e}")
    exit(1)