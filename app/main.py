from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.model.database import conectar_banco
from app.controller.rotas import router

app = FastAPI(title="API de Catálogo de Plantas 🌱")

# Caminho do arquivo da interface (front-end servido pela própria API)
FRONTEND = Path(__file__).resolve().parent / "web" / "index.html"


@app.on_event("startup")
async def startup_event():
    await conectar_banco()


app.include_router(router)


@app.get("/", include_in_schema=False)
def home():
    # Serve a interface amigável para o usuário final.
    return FileResponse(FRONTEND)


@app.get("/api")
def api_info():
    return {"mensagem": "API de plantas no ar! 🌿"}
