from fastapi import FastAPI, status
from app.scraper import save_info, get_info  # Importa as funções do scraper

app = FastAPI()

# Endpoint para salvar informações no MongoDB
@app.post("/save_info", status_code=status.HTTP_201_CREATED)
async def save(url: str):
    return await save_info(url)  # Chama a função para salvar informações

# Endpoint para obter informações do MongoDB
@app.get("/get_info")
async def get(url: str):
    return await get_info(url)  # Chama a função para obter informações

# Inicializa o servidor usando uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)
