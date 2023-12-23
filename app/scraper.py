import requests
from bs4 import BeautifulSoup
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
import os
import uuid  # Importa a biblioteca para gerar UUIDs

MONGODB_URL = os.getenv("MONGODB_URL")  # Carrega a URL do MongoDB a partir das variáveis de ambiente

# Conexão com o MongoDB
client = AsyncIOMotorClient(MONGODB_URL)
db = client['quotes']
collection = db['quotes_01']

# Função para fazer o scraping das citações
async def scrape_quotes(url):
    url = 'http://quotes.toscrape.com/'  # URL específica do site para scraping
    try:
        response = requests.get(url)  # Faz a requisição HTTP para a URL
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    except requests.RequestException as e:
        # Se houver um erro na requisição, levanta uma exceção HTTP 400
        raise HTTPException(status_code=400, detail=f"Error: {e}")

    # Analisa a resposta HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes = []

    # Encontra todas as caixas de citação na página
    quote_boxes = soup.find_all("div", class_="quote")

    # Itera sobre cada caixa de citação encontrada
    for quote_box in quote_boxes:
        text = quote_box.find("span", class_="text").text  # Extrai o texto da citação
        author = quote_box.find("small", class_="author").text  # Extrai o autor da citação
        tags = [tag.text for tag in quote_box.find_all("a", class_="tag")]  # Extrai as tags da citação

        # Gera um ID único para a citação usando UUID
        quote_id = str(uuid.uuid4())

        # Armazena as informações em um dicionário para cada citação
        quote_info = {
            'id': quote_id,
            'text': text,
            'author': author,
            'tags': tags,
        }

        # Adiciona as informações da citação à lista de citações
        quotes.append(quote_info)

    # Retorna um dicionário com a URL da página e as citações extraídas
    return {
        'url': url,
        'quotes': quotes,
    }

# Função para salvar informações no MongoDB
async def save_info(url):
    url = url.strip().rstrip("/")  # Padroniza a URL removendo espaços em branco e barras finais
    data = await scrape_quotes(url)  # Chama a função de scraping
    await collection.insert_one(data)  # Insere os dados no MongoDB
    return {"Mensagem": "Quotes Salvas Com Sucesso"}  # Retorna uma mensagem de sucesso

# Função para obter informações do MongoDB
async def get_info(url):
    url = url.strip().rstrip("/")  # Padroniza a URL removendo espaços em branco e barras finais
    data = await collection.find_one({"url": url})  # Procura os dados no MongoDB
    if not data:
        raise HTTPException(status_code=404, detail="Not Found")  # Se não encontrar, levanta uma exceção HTTP 404
    return {"url": data.get("url"), "quotes": data.get("quotes")}  # Retorna os dados encontrados
