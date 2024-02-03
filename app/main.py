 
# app/main.py
from fastapi import FastAPI
from app.api.endpoints import user_endpoint, role_endpoint, post_endpoint, hasil_endpoint, gejala_endpoint, penyakit_endpoint, basis_pengetahuan_endpoint, kondisi_endpoint

app = FastAPI()

app.include_router(user_endpoint.router, prefix="/api")
app.include_router(gejala_endpoint.router, prefix="/api")
app.include_router(penyakit_endpoint.router, prefix="/api")
app.include_router(basis_pengetahuan_endpoint.router, prefix="/api")
app.include_router(kondisi_endpoint.router, prefix="/api")
app.include_router(hasil_endpoint.router, prefix="/api")
app.include_router(post_endpoint.router, prefix="/api")
app.include_router(role_endpoint.router, prefix="/api")
