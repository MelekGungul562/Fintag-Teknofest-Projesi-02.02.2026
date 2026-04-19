"""
FINTAG Backend - Veri Modelleri (Pydantic)
Kredi başvurusu ve tahmin için veri yapıları
"""

from pydantic import BaseModel, Field
from typing import Optional


class LoanApplicationInput(BaseModel):
    """Kredi başvurusu giriş modeli"""
    
    # Demografik bilgiler
    age: int = Field(..., ge=18, le=100, description="Başvurucu yaşı")
    gender: str = Field(..., description="Cinsiyet (M/F)")
    education: str = Field(..., description="Eğitim Seviyesi")
    marital_status: str = Field(..., description="Medeni Durum")
    
    # Finansal bilgiler
    annual_income: float = Field(..., gt=0, description="Yıllık gelir (TL)")
    monthly_expense: float = Field(..., ge=0, description="Aylık gider (TL)")
    credit_score: int = Field(..., ge=0, le=1000, description="Kredi skoru")
    employment_years: int = Field(..., ge=0, description="İş deneyimi (yıl)")
    
    # Kredi bilgileri
    loan_amount: float = Field(..., gt=0, description="İstenen kredi miktarı (TL)")
    loan_term: int = Field(..., ge=1, le=360, description="Kredi terimi (ay)")
    credit_history: str = Field(..., description="Kredi geçmişi")
    
    class Config:
        schema_extra = {
            "example": {
                "age": 35,
                "gender": "M",
                "education": "Bachelor",
                "marital_status": "Married",
                "annual_income": 120000,
                "monthly_expense": 5000,
                "credit_score": 750,
                "employment_years": 10,
                "loan_amount": 50000,
                "loan_term": 60,
                "credit_history": "Good"
            }
        }


class PredictionOutput(BaseModel):
    """Model tahmin çıktı modeli"""
    
    prediction: int = Field(..., description="Tahmin (0: Red, 1: Onay)")
    probability: float = Field(..., ge=0, le=1, description="Onay olasılığı (0-1)")
    risk_level: str = Field(..., description="Risk seviyesi (Düşük/Orta/Yüksek)")
    explanation: dict = Field(..., description="SHAP açıklamaları")


class ExplanationRequest(BaseModel):
    """XAI açıklama isteği"""
    
    loan_application: LoanApplicationInput
    top_features: int = Field(default=10, ge=1, le=15, description="Gösterilecek özellik sayısı")
