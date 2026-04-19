"""
FINTAG - SHAP Açıklanabilirlik Yardımcıları
Model kararlarının açıklanması için SHAP entegrasyonu
"""

import shap
import numpy as np
import pandas as pd
from typing import Dict, List


class SHAPExplainer:
    """SHAP ile model açıklanabilirliği"""
    
    def __init__(self, model, X_data: pd.DataFrame):
        """
        SHAP explainer başlatılması
        
        Args:
            model: Eğitilmiş makine öğrenmesi modeli
            X_data: Eğitim veri seti (arka plan verileri)
        """
        self.model = model
        self.X_data = X_data
        self.explainer = shap.TreeExplainer(model)
        self.shap_values = None
    
    def explain_single_prediction(self, sample: pd.DataFrame) -> Dict:
        """
        Tek bir tahmin için açıklama üretme
        
        Args:
            sample: Tek bir veri satırı
        
        Returns:
            Dict: SHAP açıklama değerleri ve metadata
        """
        self.shap_values = self.explainer.shap_values(sample)
        
        # Positive class için SHAP values (Kredi onayı)
        shap_vals = self.shap_values[1][0] if isinstance(self.shap_values, list) else self.shap_values[0]
        
        feature_importance = {
            self.X_data.columns[i]: float(shap_vals[i])
            for i in range(len(self.X_data.columns))
        }
        
        # En etkili özellikler (pozitif ve negatif)
        sorted_importance = sorted(
            feature_importance.items(), 
            key=lambda x: abs(x[1]), 
            reverse=True
        )
        
        return {
            "base_value": float(self.explainer.expected_value[1]),
            "feature_contributions": feature_importance,
            "top_positive_features": [f for f, v in sorted_importance[:5] if v > 0],
            "top_negative_features": [f for f, v in sorted_importance[:5] if v < 0],
            "sorted_features": sorted_importance
        }
    
    def get_global_feature_importance(self) -> Dict:
        """
        Global feature importance hesaplama
        
        Returns:
            Dict: Tüm veri seti için özellik önemleri
        """
        self.shap_values = self.explainer.shap_values(self.X_data)
        
        # Positive class için ortalama SHAP values
        shap_vals = np.abs(self.shap_values[1] if isinstance(self.shap_values, list) else self.shap_values).mean(axis=0)
        
        importance = {
            self.X_data.columns[i]: float(shap_vals[i])
            for i in range(len(self.X_data.columns))
        }
        
        return dict(sorted(importance.items(), key=lambda x: x[1], reverse=True))
