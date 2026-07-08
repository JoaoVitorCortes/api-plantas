from fastapi import APIRouter

from app.services.servicos import (
  servico_criar_planta,
  servico_listar_plantas,
  servico_buscar_plantas_id,
  servico_editar_planta,
  servico_deletar_planta,
  servico_regar_planta,
)
from app.views.validacoes import(
  CriarPlanta,
  EditarPlanta,
  RespostaPlanta,
)

router = APIRouter(prefix="/plantas", tags=["Plantas"])

@router.post("/", response_model=RespostaPlanta, status_code=201)
async def criar_planta(dados: CriarPlanta):
    return await servico_criar_planta(dados_planta=dados)

@router.get("/", response_model=list[RespostaPlanta])
async def listar_plantas(quantidade: int=10):
  return await servico_listar_plantas(quantidade=quantidade)

@router.get("/{id}", response_model=RespostaPlanta)
async def buscar_planta(id: str):
  return await servico_buscar_plantas_id(id=id)

@router.put("/{id}", response_model=RespostaPlanta)
async def editar_planta(id: str, dados: EditarPlanta):
  return await servico_editar_planta(id=id, dados_planta=dados)

@router.patch("/{id}/regar", response_model=RespostaPlanta)
async def regar_planta(id: str):
    return await servico_regar_planta(id=id)

@router.delete("/{id}")
async def deletar_planta(id: str):
  return await servico_deletar_planta (id=id)