from flask import Flask, render_template_string
import requests

app = Flask(__name__)

#Função para buscar as cotações
def cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url)  # Faz a requisição à API
        
        data = response.json()  # Converte a resposta para JSON

        # Retorna as cotações
        return {
            "USD": data["USDBRL"]["bid"],
            "EUR": data["EURBRL"]["bid"],
            "BTC": data["BTCBRL"]["bid"],
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar-se à API: {e}")
        return {
            "USD": "N/A",
            "EUR": "N/A",
            "BTC": "N/A",
        }

#Define a rota principal
@app.route("/")
def home():
    rates = cotacoes()
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cotações do Dia</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                text-align: center;
                background-color: #f4f4f9;
            }
            h1 {
                color: #333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
                font-size: 1.2em;
            }
        </style>
    </head>
    <body>
        <h1>Cotações do Dia</h1>
        <ul>
            <li><strong>Dólar (USD/BRL):</strong> R$ {{ rates['USD'] }}</li>
            <li><strong>Euro (EUR/BRL):</strong> R$ {{ rates['EUR'] }}</li>
            <li><strong>Bitcoin (BTC/BRL):</strong> R$ {{ rates['BTC'] }}</li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, rates=rates)

if __name__ == "__main__":
    app.run(debug=True)