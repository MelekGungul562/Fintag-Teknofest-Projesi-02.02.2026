"""
FINTAG - Model Eğitim Yardımcı Fonksiyonları
Veri ön işleme, model eğitimi ve değerlendirme
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    classification_report, confusion_matrix, 
    roc_auc_score, f1_score, precision_score, recall_score
)
import joblib
from typing import Tuple, Dict


def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    """
    Veri seti yükleme ve ilk kontroller
    
    Args:
        filepath: CSV dosyasının yolu
    
    Returns:
        DataFrame: Yüklenen veri seti
    """
    print(f"Veri seti yükleniyor: {filepath}")
    df = pd.read_csv(filepath)
    print(f"Veri seti şekli: {df.shape}")
    print(f"Eksik veriler:\n{df.isnull().sum()}")
    return df


def evaluate_model(y_true, y_pred, y_pred_proba: np.ndarray = None) -> Dict:
    """
    Model performansını değerlendirme
    
    Args:
        y_true: Gerçek etiketler
        y_pred: Tahminler
        y_pred_proba: Tahmin olasılıkları
    
    Returns:
        Dict: Metrik sonuçları
    """
    metrics = {
        "f1_score": f1_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "classification_report": classification_report(y_true, y_pred)
    }
    
    if y_pred_proba is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_pred_proba[:, 1])
    
    print("=" * 50)
    print("MODEL DEĞERLENDİRME")
    print("=" * 50)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    return metrics


def save_model(model, filepath: str):
    """Model kaydetme"""
    joblib.dump(model, filepath)
    print(f"Model kaydedildi: {filepath}")


def load_model(filepath: str):
    """Model yükleme"""
    model = joblib.load(filepath)
    print(f"Model yüklendi: {filepath}")
    return model
