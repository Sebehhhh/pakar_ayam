# app/main.py
from fastapi import FastAPI
from app.api.endpoints import login_endpoint, user_endpoint, role_endpoint, post_endpoint, hasil_endpoint, gejala_endpoint, penyakit_endpoint, basis_pengetahuan_endpoint, kondisi_endpoint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Menambahkan middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Atur domain Anda di sini
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(user_endpoint.router, prefix="/api")
app.include_router(gejala_endpoint.router, prefix="/api")
app.include_router(penyakit_endpoint.router, prefix="/api")
app.include_router(basis_pengetahuan_endpoint.router, prefix="/api")
app.include_router(kondisi_endpoint.router, prefix="/api")
app.include_router(hasil_endpoint.router, prefix="/api")
app.include_router(post_endpoint.router, prefix="/api")
app.include_router(role_endpoint.router, prefix="/api")
app.include_router(login_endpoint.router, prefix="/api")
