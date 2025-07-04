import pandas as pd
from pathlib import Path

CSV_PATH = Path("data/DENGBR24_processed.csv")

def load_filtered_data(city, state, start_date, end_date):
    try:
        df = pd.read_csv(CSV_PATH)

        for col in df.columns:
            if "Data" in col:
                df[col] = pd.to_datetime(df[col], errors="coerce")

        if city:
            df = df[df["Município da Notificação"].str.contains(city, case=False, na=False)]

        if state:
            df = df[df["UF da Notificação"].str.upper() == state.upper()]

        if start_date:
            df = df[df["Data de Notificação"] >= pd.to_datetime(start_date)]

        if end_date:
            df = df[df["Data de Notificação"] <= pd.to_datetime(end_date)]

        df = df.fillna(0)

        return df.where(pd.notnull(df), None).to_dict(orient="records")

    except Exception as e:
        return {"erro": str(e)}
