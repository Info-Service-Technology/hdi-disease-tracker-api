from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class DengueCase(BaseModel):
    agravo: Optional[str] = Field(None, description="Tipo de agravo notificado", example="Dengue")
    sexo: Optional[str] = Field(None, description="Sexo", example="Masculino")
    gestante: Optional[str] = Field(None, description="Gestante", example="Não")
    raca: Optional[str] = Field(None, description="Raça", example="Branca")
    uf_notificacao: Optional[str] = Field(None, description="UF da Notificação", example="Rio de Janeiro")
    municipio_notificacao: Optional[str] = Field(None, description="Município da Notificação", example="Petrópolis")
    municipio_residencia: Optional[str] = Field(None, description="Município de Residência", example="Desconhecido")
    data_notificacao: Optional[date] = Field(None, description="Data de Notificação", example="2024-10-24")