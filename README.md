# <img src="https://i.imgur.com/gl5r9LJ.png" alt="Logo" width="30" style="margin-right: 8px; vertical-align: middle;"/> Health Data Insights - Petrópolis (RJ)

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
  git clone https://github.com/PedroDutra86/hdi-disease-tracker-api.git
  cd hdi-disease-tracker-api
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

## 🐳 Docker Setup

You can run the API using Docker without manually installing any dependencies.
The Docker image for this project is available on [Docker Hub](https://hub.docker.com/repository/docker/pedrodutra86/hdi-api/general).

You can pull the image using:
  ```bash
  docker pull pedrodutra86/hdi-api
  ```

### Prerequisites

- Docker and Docker Compose installed
- Docker Desktop running

### Build and run the container

1. Clone the repository:
  ```bash
  git clone https://github.com/PedroDutra86/hdi-disease-tracker-api.git
  cd hdi-disease-tracker-api
  ```

2. Build and start the API:
  ```bash
  docker-compose up --build
  ```

3. Access the API documentation at: http://localhost:8000/docs

### Updating the data

To update the API data:

1. Replace the CSV file in api/data/ with the new file.
2. Restart the container:
  ```bash
  docker-compose restart
  ```

The API will automatically use the updated CSV file.

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

## 🛡️ Test Documentation

This project includes automated tests to ensure the API is functioning correctly. The tests are performed using the **pytest** framework and are based on the API routes implemented.

### How to Run Tests

To run the tests, follow the steps below:

1. **Install the project dependencies:**

  If you haven't done this already, install the necessary dependencies with the command:

  ```bash
  pip install -r requirements.txt
  ```

2. **Run the tests:**

  To run the tests, execute the following command:

  ```bash
  pytest
  ```

  pytest will automatically search for test files in the `tests/` folder and execute them.

### Test Structure

The tests are located in the `tests/` folder. Each test file follows the convention `test_<feature_name>.py`. Currently, the following tests are implemented:

#### Tests for the `/dengue` endpoint

- **test_read_root**: Verifies if the root route (`/`) returns the expected response with status 200 and the message "HDI API is running".
- **test_get_dengue_data**: Verifies if the `/dengue` endpoint with `limit` and `skip` parameters returns the data correctly.
- **test_filter_by_city**: Verifies if the filter by city in the `/dengue` endpoint works correctly.
- **test_limit_and_skip**: Verifies if the `limit` and `skip` parameters work properly when paginating the results.

#### Tests for the `/dengue` endpoint with filter parameters

- **test_skip_greater_than_total**: Verifies the behavior when the `skip` value is greater than the total number of available records. The response is expected to be an empty list.
  
### Test Coverage

Currently, the tests cover the main features of the `/dengue` endpoint, such as filter parameters, pagination, and data validation.

### Running Specific Tests

If you want to run a specific test, you can use the following command:

  ```bash
  pytest -k <test_name>
  ```