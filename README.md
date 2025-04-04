# Health Data Insights - Petrópolis (RJ)

This repository contains a **FastAPI**-based API that exposes processed **dengue** case data for the municipality of **Petrópolis, Rio de Janeiro, Brazil**.

## 🔍 Purpose

To provide a publicly accessible data API for analysis, visualization, and monitoring of dengue cases in Petrópolis-RJ. The API can be integrated into dashboards or used for predictive analytics.

## 🚀 Tech Stack

- Python 3.12
- FastAPI
- Pandas
- Uvicorn
- CORS Middleware

## 📦 Running Locally

1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/Health-Data-Insights-Petropolis.git
  cd Health-Data-Insights-Petropolis
  ```

2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  - Linux/Mac
  .\venv\Scripts\activate   - Windows
  ```

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the server:
  ```bash
  uvicorn main:app --reload
  ```

5. Access the automatic API documentation:
  http://localhost:8000/docs

## 📊 Query Parameters

The `/dengue` endpoint supports the following optional filters:

| Parameter               | Description                                      |
|-------------------------|--------------------------------------------------|
| `agravo`                | Type of disease reported                         |
| `sexo`                  | Patient's gender                                 |
| `gestante`              | Pregnancy status                                 |
| `raca`                  | Race/color                                       |
| `uf_notificacao`        | Notification state                               |
| `municipio_notificacao` | Notification city                                |
| `unidade_saude`         | Health unit that reported the case               |
| `uf_residencia`         | State of residence                               |
| `municipio_residencia`  | City of residence                                |
| `pais_residencia`       | Country of residence                             |
| `data_notificacao`      | Notification date (format: `YYYY-MM-DD`)        |
| `data_inicio_sintomas`  | Symptom onset date (format: `YYYY-MM-DD`)       |

## 📌 Pagination

| Parameter | Description                                  |
|-----------|----------------------------------------------|
| `skip`    | Number of records to skip (default: `0`)     |
| `limit`   | Maximum number of records per page (default: `10`) |