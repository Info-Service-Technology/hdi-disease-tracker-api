from fastapi import APIRouter, Query
import pandas as pd
from pathlib import Path

router = APIRouter()

CSV_PATH = Path("data/DENGBR24_processed.csv")

@router.get("/dengue")
def get_dengue_data(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1)):
    try:
        df = pd.read_csv(CSV_PATH)

        for col in df.columns:
            if "Data" in col:
                df[col] = df[col].astype(str)

        df = df.fillna(0)

        records = df.where(pd.notnull(df), None).to_dict(orient="records")
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
