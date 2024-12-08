# Importação de bibliotecas
import streamlit as st
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import json

# Configuração do título da página
st.set_page_config(page_title="NucleAI", page_icon="🌐")

# Configuração do CSS para ajustar tamanho da fonte e altura da caixa de input
st.markdown(
    """
    <style>
    /* Aumentando o tamanho da fonte da página */
    body {
        font-size: 30px; 
    }
    h1 {
        font-size: 60px;
    }
    p {
        font-size: 20px;
    }

    /* Ajustando a altura da caixa de input do chat */
    div.stChatInput div textarea {
        height: 100px !important; 
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Função para interagir com o modelo da AWS Titan
def query_aws_titan(prompt, access_key, secret_key, region):
    try:
        # Criar cliente do Amazon Bedrock (AWS Titan é gerido por Bedrock)
        client = boto3.client(
            'bedrock-runtime',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

        # Configurar o payload da requisição
        response = client.invoke_model(
            modelId='amazon.titan-text-premier-v1:0',  # ID do modelo AWS Titan
            body=json.dumps({"inputText": prompt}).encode("utf-8"),
            contentType="application/json"
        )

        # Processar a resposta
        response_body = response['body'].read()
        response_json = json.loads(response_body.decode('utf-8'))  # Decode JSON

        if 'results' in response_json and response_json['results']:
            output_text = response_json['results'][0].get('outputText', 'Desculpe, não entendi.')
            return output_text
        else:
            return "Desculpe, não entendi."


    except (BotoCoreError, ClientError) as error:
        st.error("Erro ao se comunicar com a API da AWS Titan")
        return str(error)


# Título e descrição
st.title("NucleAI")
st.write("Bem-vindo ao NucleAI! Converse com nosso chatbot")

# Área para entrada de credenciais da AWS (somente para testes locais)
with st.sidebar:
    st.header("Configurações da AWS")
    aws_access_key = st.text_input("AWS Access Key", type="password")
    aws_secret_key = st.text_input("AWS Secret Key", type="password")
    aws_region = st.text_input("AWS Region", value="us-east-1")

# Entrada de mensagem do usuário
if prompt := st.chat_input("Digite sua mensagem"):
    with st.spinner("Aguardando resposta..."):
        if not aws_access_key or not aws_secret_key:
            st.error("Por favor, configure as credenciais da AWS na barra lateral")
        else:
            response = query_aws_titan(prompt, aws_access_key, aws_secret_key, aws_region)
            st.write("**Você:**", prompt)
            st.write("**NucleAI:**", response)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️ pela equipe NucleAI.")
