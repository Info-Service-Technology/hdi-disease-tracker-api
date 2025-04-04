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