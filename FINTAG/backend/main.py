"""
FINTAG - Kredi Risk Analiz Sistemi
FastAPI Backend Uygulaması
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

# Logging konfigürasyonu
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI uygulaması
app = FastAPI(
    title="FINTAG API",
    description="Yapay Zeka Destekli Kredi Risk Analiz Sistemi",
    version="1.0.0",
)

# CORS middleware konfigürasyonu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """API sağlık kontrolü"""
    return {
        "message": "FINTAG Backend aktif ve çalışıyor",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Sistem sağlık durumu"""
    return {
        "status": "healthy",
        "service": "FINTAG Credit Risk Analysis System"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
