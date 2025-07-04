from fastapi import APIRouter, Query, HTTPException
from typing import Optional
import pandas as pd
from pathlib import Path

router = APIRouter()

CSV_PATH = Path("data/DENGBR24_processed.csv")
try:
    df_global = pd.read_csv(CSV_PATH)
    for col in df_global.columns:
        if "Data" in col:
            df_global[col] = df_global[col].astype(str)
except FileNotFoundError:
    df_global = None

@router.get("/dengue")
def get_dengue_data(
    skip: int = Query(0, ge=0, description="Número de registros a pular"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros retornados"),
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
):
    if df_global is None:
        raise HTTPException(status_code=500, detail="Arquivo de dados não encontrado")

    df = df_global.copy()

    try:
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

        df = df.fillna(0)
        total = len(df)
        data = df.iloc[skip : skip + limit].to_dict(orient="records")

        return {
            "total": total,
            "page_size": limit,
            "page_start": skip,
            "page_end": min(skip + limit, total),
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
