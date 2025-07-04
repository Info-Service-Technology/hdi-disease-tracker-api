FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expor a porta padrão do Elastic Beanstalk (geralmente 8080)
EXPOSE 8080

# Usar variável de ambiente PORT para definir a porta onde o Uvicorn vai escutar
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]

