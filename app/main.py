from fastapi import FastAPI
from app.model.database import conectar_banco
from app.controller.rotas import router

app = FastAPI(title="API de Catálogo de Plantas 🌱")


@app.on_event("startup")
async def startup_event():
    await conectar_banco()


app.include_router(router)


@app.get("/")
def home():
    return {"mensagem": "API de plantas no ar! 🌿"}