from fastapi import HTTPException
from app.views.validacoes import RespostaPlanta
from app.model.modelos import (
  modelo_criar_planta,
  modelo_listar_plantas,
  modelo_buscar_plantas_id,
  modelo_editar_planta,
  modelo_deletar_planta
)
from app.utils.data_atual import data_atual 
from app.utils.parser import parser_id_mongo, parser_lista_ids_mongo


async def servico_criar_planta(dados_planta):
  data = data_atual()
  dados_modelo = {
    "nome": dados_planta.nome,
    "especie":dados_planta.especie, 
    "frequencia_rega_dias": dados_planta.frequencia_rega_dias,
    "exposicao_solar": dados_planta.exposicao_solar,
    "ambiente": dados_planta.ambiente,
    "criado_em": data,
    "atualizado_em": data,
    "ultima_rega": data,
    "observacoes": dados_planta.observacoes,
  }
  modelo_planta = await modelo_criar_planta(dados_modelo=dados_modelo)
  return RespostaPlanta(**parser_id_mongo(modelo_planta))

async def servico_listar_plantas(quantidade):
  plantas = await modelo_listar_plantas(quantidade=quantidade)
  lista_dicts = parser_lista_ids_mongo(plantas)
  return [RespostaPlanta(**item) for item in lista_dicts]

async def servico_buscar_plantas_id(id):
  planta = await modelo_buscar_plantas_id(id=id)
  if planta is None:
    raise HTTPException(status_code=404, detail="Planta não encontrada. Essa teria que plantar!")
  return RespostaPlanta(**parser_id_mongo(planta))

async def servico_editar_planta(id, dados_planta):
  dados_modelo = dados_planta.dict(exclude_unset=True)
  dados_modelo["atualizado_em"] = data_atual()
  planta = await modelo_editar_planta(id=id, dados_modelo=dados_modelo)
  if planta is None:
    raise HTTPException(status_code=404, detail="Planta não encontrada. Tente editar outra ou revisar o ID!")
  return RespostaPlanta(**parser_id_mongo(planta))

async def servico_regar_planta(id):
  dados_modelo = {"ultima_rega": data_atual()}
  planta = await modelo_editar_planta(id=id, dados_modelo=dados_modelo)
  if planta is None:
      raise HTTPException(status_code=404, detail="Não foi possível marcar como regada.")
  return RespostaPlanta(**parser_id_mongo(planta))

async def servico_deletar_planta(id):
  mensagem = await modelo_deletar_planta(id=id)
  if mensagem is None:
    raise HTTPException(status_code=404, detail="Planta não encontrada ou já foi deletada!")
  return mensagem