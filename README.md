# Web Scraper e API FastAPI para Salvamento e Recuperação de Citações

Site utilizado no lugar do site SimilarWeb pois o mesmo não aceita práticas de scrapy em seu site, logo peguei um site de exemplo, sendo possível apenas atualizando a função da raspagem utilizá-la em outros sites e aplicações.

Este projeto é uma aplicação FastAPI para realizar scraping de citações de um site e salvar os dados em um banco de dados MongoDB.

## Funcionalidades

- **save_info:** Endpoint para realizar o scraping de citações a partir de uma URL fornecida e salvar os dados no MongoDB.

Exemplo de Uso do Endpoint /save_info
Para salvar informações de citações do site http://quotes.toscrape.com/, utilize o seguinte formato de URL para fazer uma requisição POST:

http://localhost:8000/save_info?url=http%3A%2F%2Fquotes.toscrape.com%2F


- **get_info:** Endpoint para obter as citações salvas no MongoDB a partir de uma URL fornecida.

Exemplo de Uso do Endpoint /get_info
Para obter as informações de citações previamente salvas do site http://quotes.toscrape.com/, utilize o seguinte formato de URL para fazer uma requisição GET:

http://localhost:8000/get_info?url=http%3A%2F%2Fquotes.toscrape.com%2F

Isso fará uma chamada ao endpoint /get_info, enviando a mesma URL http://quotes.toscrape.com/ como parâmetro. 

## Configuração

1. Instale as dependências do projeto:
pip install -r requirements.txt


2. Defina as variáveis de ambiente no arquivo `.env`:
MONGODB_URL=your_mongodb_connection_url


3. Execute o servidor localmente:
uvicorn app.main:app --reload


## Estrutura do Projeto

projeto/
├── app/
│ ├── init.py
│ ├── main.py
│ └── scraper.py
├── .env
├── README.md
└── requirements.txt



- **`app/`:** Contém o código principal da aplicação.
- **`main.py`:** Arquivo principal da aplicação FastAPI.
- **`scraper.py`:** Contém funções relacionadas ao scraping de citações.
- **`.env`:** Arquivo de variáveis de ambiente (não deve ser enviado para o repositório).
- **`README.md`:** Este arquivo que contém informações sobre o projeto.

## Contribuição

- Sinta-se à vontade para contribuir com melhorias ou correções de bugs.
