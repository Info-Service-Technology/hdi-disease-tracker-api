from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import dengue

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dengue.router)

@app.get("/")
def read_root():
    return {"message": "HDI API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
