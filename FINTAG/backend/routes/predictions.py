"""
FINTAG - Backend Giriş Noktası
Kredi Tahmin Routes
"""

from fastapi import APIRouter, HTTPException
from ..models import LoanApplicationInput, PredictionOutput
import pickle
import os

router = APIRouter(prefix="/api", tags=["predictions"])


@router.post("/predict", response_model=PredictionOutput)
async def predict_loan(application: LoanApplicationInput):
    """
    Kredi başvurusunu tahmin et.
    
    - **age**: Başvurucu yaşı
    - **annual_income**: Yıllık gelir
    - **loan_amount**: İstenen kredi miktarı
    """
    try:
        # Model yükleme
        model_path = "ml_models/models/best_model.pkl"
        if not os.path.exists(model_path):
            raise HTTPException(status_code=500, detail="Model bulunamadı")
        
        # TODO: Model tahmin mantığı
        # Şu anda placeholder response döndürülüyor
        
        return PredictionOutput(
            prediction=1,
            probability=0.75,
            risk_level="Düşük",
            explanation={
                "primary_factors": ["Yüksek Gelir", "İyi Kredi Skoru"],
                "risk_indicators": ["Yüksek Borç Oranı"]
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/explain")
async def explain_prediction(application: LoanApplicationInput):
    """
    Kredi tahmininin SHAP açıklamasını sağla.
    
    XAI (Açıklanabilir Yapay Zeka) analizi döndürür.
    """
    try:
        # TODO: SHAP açıklama mantığı
        return {
            "message": "SHAP açıklama endpoint'i - Geliştirme aşamasında",
            "feature_contributions": {},
            "most_important_features": []
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
