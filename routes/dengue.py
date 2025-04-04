from fastapi import APIRouter, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import pandas as pd
from pathlib import Path

router = APIRouter()


CSV_PATH = Path("data/DENGBR24_processed.csv")

@router.get("/dengue")
def get_dengue_data(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    agravo: Optional[str] = None,
    sexo: Optional[str] = None,
    gestante: Optional[str] = None,
    raca: Optional[str] = None,
    uf_notificacao: Optional[str] = Query(None, alias="uf_notificacao"),
    municipio_notificacao: Optional[str] = Query(None, alias="municipio_notificacao"),
    unidade_saude: Optional[str] = Query(None, alias="unidade_saude"),
    uf_residencia: Optional[str] = Query(None, alias="uf_residencia"),
    municipio_residencia: Optional[str] = Query(None, alias="municipio_residencia"),
    pais_residencia: Optional[str] = Query(None, alias="pais_residencia"),
    data_inicio_sintomas: Optional[str] = None,
    data_notificacao: Optional[str] = None,
    data_nascimento: Optional[str] = None,
    data_internacao: Optional[str] = None,
    idade: Optional[int] = None,
    faixa_etaria: Optional[str] = None,
    escolaridade: Optional[str] = None,
    classificacao_final: Optional[str] = None,
    evolucao_caso: Optional[str] = None,
    criterio_confirmacao: Optional[str] = None,
    tipo_atendimento: Optional[str] = None,
    tipo_notificacao: Optional[str] = None,
    profissional_notificante: Optional[str] = None,
    municipio_atendimento: Optional[str] = None,
):
    try:
        df = pd.read_csv(CSV_PATH)

        for col in df.columns:
            if "Data" in col:
                df[col] = df[col].astype(str)

        if agravo: df = df[df["Agravo"] == agravo]
        if sexo: df = df[df["Sexo"] == sexo]
        if gestante: df = df[df["Gestante"] == gestante]
        if raca: df = df[df["Raça"] == raca]
        if uf_notificacao: df = df[df["UF da Notificação"] == uf_notificacao]
        if municipio_notificacao: df = df[df["Município da Notificação"] == municipio_notificacao]
        if unidade_saude: df = df[df["Unidade de Saúde"] == unidade_saude]
        if uf_residencia: df = df[df["UF de Residência"] == uf_residencia]
        if municipio_residencia: df = df[df["Município de Residência"] == municipio_residencia]
        if pais_residencia: df = df[df["País de Residência"] == pais_residencia]
        if data_inicio_sintomas: df = df[df["Data de Início dos Sintomas"] == data_inicio_sintomas]
        if data_notificacao: df = df[df["Data da Notificação"] == data_notificacao]
        if data_nascimento: df = df[df["Data de Nascimento"] == data_nascimento]
        if data_internacao: df = df[df["Data da Internação"] == data_internacao]
        if idade: df = df[df["Idade"] == idade]
        if faixa_etaria: df = df[df["Faixa Etária"] == faixa_etaria]
        if escolaridade: df = df[df["Escolaridade"] == escolaridade]
        if classificacao_final: df = df[df["Classificação Final"] == classificacao_final]
        if evolucao_caso: df = df[df["Evolução do Caso"] == evolucao_caso]
        if criterio_confirmacao: df = df[df["Critério de Confirmação"] == criterio_confirmacao]
        if tipo_atendimento: df = df[df["Tipo de Atendimento"] == tipo_atendimento]
        if tipo_notificacao: df = df[df["Tipo de Notificação"] == tipo_notificacao]
        if profissional_notificante: df = df[df["Profissional Notificante"] == profissional_notificante]
        if municipio_atendimento: df = df[df["Município de Atendimento"] == municipio_atendimento]

        df = df.fillna(0)
        records = df.to_dict(orient="records")
        total = len(records)

        return {
            "total": total,
            "page_size": limit,
            "page_start": skip,
            "page_end": min(skip + limit, total),
            "data": records[skip:skip+limit]
        }

    except Exception as e:
        return {"erro": str(e)}
