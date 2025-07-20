import boto3
import time
from fastapi import APIRouter, Query, HTTPException
from typing import Optional

router = APIRouter()

# Inicializa cliente Athena
athena_client = boto3.client('athena', region_name='sa-east-1')  # ajuste a região conforme seu bucket

DATABASE = 'dados_hdi_db'  # ajuste no seu Glue/Athena
OUTPUT_BUCKET = 's3://dados-hdi/'  # bucket S3 onde Athena armazena resultados

def execute_athena_query(query):
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': DATABASE},
        ResultConfiguration={'OutputLocation': OUTPUT_BUCKET}
    )
    query_execution_id = response['QueryExecutionId']

    # Aguardar query terminar
    while True:
        query_status = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        state = query_status['QueryExecution']['Status']['State']
        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(1)

    if state != 'SUCCEEDED':
        raise Exception(f'Athena query failed or cancelled with status: {state}')

    results = athena_client.get_query_results(QueryExecutionId=query_execution_id)
    return results
@router.get("/dengue")
def get_dengue_data(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
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
    tipo_notificacao: Optional[str] = Query(None, alias="tipo_notificacao")
):
    try:
        filters = []
        if agravo:
            filters.append(f"agravo = '{agravo}'")
        if sexo:
            filters.append(f"sexo = '{sexo}'")
        if gestante:
            filters.append(f"gestante = '{gestante}'")
        if raca:
            filters.append(f"raca = '{raca}'")
        if uf_notificacao:
            filters.append(f"uf_da_notificacao = '{uf_notificacao}'")
        if municipio_notificacao:
            filters.append(f"municipio_da_notificacao = '{municipio_notificacao}'")
        if unidade_saude:
            filters.append(f"unidade_de_saude = '{unidade_saude}'")
        if uf_residencia:
            filters.append(f"uf_de_residencia = '{uf_residencia}'")
        if municipio_residencia:
            filters.append(f"municipio_de_residencia = '{municipio_residencia}'")
        if pais_residencia:
            filters.append(f"pais_de_residencia = '{pais_residencia}'")
        if tipo_notificacao:
            filters.append(f"tipo_notificacao = '{tipo_notificacao}'")
        where_clause = ''
        if filters:
            where_clause = 'WHERE ' + ' AND '.join(filters)

        # Monta query com paginação usando LIMIT e OFFSET
        query = f"""
             SELECT *
                FROM dengue_rj
                {where_clause}
                LIMIT {limit}
            """

        results = execute_athena_query(query)

        # Processar dados do resultado Athena
        # A primeira linha do results contém os metadados (colunas),
        # as seguintes são os dados efetivos.

        columns = [col['VarCharValue'] for col in results['ResultSet']['Rows'][0]['Data']]
        records = []
        for row in results['ResultSet']['Rows'][1:]:
            record = {}
            for col_idx, col_val in enumerate(row['Data']):
                record[columns[col_idx]] = col_val.get('VarCharValue', None)
            records.append(record)

        # Para total, uma query COUNT(*) pode ser executada separadamente se necessário

        return {
            "total": len(records),  # Atenção: para total correto, deve fazer query COUNT(*)
            "page_size": limit,
            "page_start": skip,
            "page_end": skip + len(records),
            "data": records
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))