import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
from app.model.modelos import Plantas

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")


async def conectar_banco():
  cliente = AsyncIOMotorClient(DATABASE_URL)
  banco = cliente[DATABASE_NAME]

  await init_beanie(
    database=banco,
    document_models=[
      Plantas,
    ],
  )

  print("Banco de Plantas Conectado com Sucesso")