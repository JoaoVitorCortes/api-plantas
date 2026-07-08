from pydantic import BaseModel
from typing import Optional


class CriarPlanta(BaseModel):
  nome: str
  especie: str
  frequencia_rega_dias: int
  exposicao_solar: str
  ambiente: str
  observacoes: Optional[str] = None

class EditarPlanta(BaseModel):
  nome: Optional[str] = None
  especie: Optional[str] = None
  frequencia_rega_dias: Optional[int] = None
  exposicao_solar: Optional[str] = None
  ambiente: Optional[str] = None
  observacoes: Optional[str] = None

class RespostaPlanta(BaseModel):
  id: str
  nome: str
  especie: str
  frequencia_rega_dias: Optional[int] = None
  exposicao_solar: Optional[str] = None
  ambiente: Optional[str] = None
  criado_em: str
  atualizado_em: str
  observacoes: Optional[str] = None
  precisa_de_rega: bool

  class Config:
    populate_by_name = True

  