from beanie import Document, PydanticObjectId
from pydantic import Field, ConfigDict
from datetime import datetime  
from typing import Optional


class Plantas(Document):
  nome: str
  especie: str
  frequencia_rega_dias: int
  exposicao_solar: str
  ambiente: str
  criado_em: datetime
  atualizado_em: datetime
  observacoes: Optional[str] = None
  ultima_rega: datetime

  class Settings:
    name = "catalogo_de_plantas"
    
  model_config = ConfigDict(
    arbitrary_types_allowed=True,
    json_encoders={datetime: lambda v: v.isoformat()}
  )


async def modelo_criar_planta(dados_modelo):
  nova_planta=Plantas(**dados_modelo)
  await nova_planta.insert()
  return nova_planta

async def modelo_listar_plantas(quantidade):
  plantas = await Plantas.find_all().limit(quantidade).to_list()
  return plantas

async def modelo_buscar_plantas_id(id: str):
  planta = await Plantas.get(id)
  return planta

async def modelo_editar_planta(id, dados_modelo):
  planta = await Plantas.get(id)
  if not planta:
      return None

  for chave, valor in dados_modelo.items():
    setattr(planta, chave, valor)
  
  await planta.save()
  return planta

async def modelo_deletar_planta(id):
  planta = await Plantas.get(id)
  if planta:
    await planta.delete()
    return f"Planta de ID: {id} deletada com sucesso"
  return None

