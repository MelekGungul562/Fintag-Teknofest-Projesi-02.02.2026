# FINTAG: Yapay Zeka Destekli Kredi Risk Analiz Sistemi

## Proje Özeti
FINTAG, geleneksel kredi değerlendirme süreçlerindeki subjektif hataları, manuel işlem yavaşlığını ve şeffaflık eksikliğini ortadan kaldırmak amacıyla geliştirilen Yapay Zeka Destekli Bir Kredi Risk Analiz Sistemidir.

## Proje Amacı
- Kullanıcıların demografik ve finansal verilerini makine öğrenmesi algoritmalarıyla analiz ederek kredi başvurularının onaylanma ihtimalini tahmin etmek
- Açıklanabilir Yapay Zeka (XAI) tekniklerini sürece dahil ederek modelin kararlarını analiz etmek
- Denetlenebilir ve güvenilir bir finansal analiz altyapısı sağlamak

## Teknoloji Stack

### Frontend
- **Framework:** React.js (Virtual DOM, bileşen tabanlı mimari)
- **Styling:** Tailwind CSS (Utility-first yaklaşımı)
- **Editor:** VS Code + GitHub Copilot

### Backend
- **Dil:** Python
- **Framework:** FastAPI (Asenkron, yüksek performans, otomatik Swagger UI)
- **Veri İşleme:** Pandas, NumPy

### Makine Öğrenmesi & XAI
- **Algoritmaları:** XGBoost, Random Forest, CatBoost (Ensemble Learning)
- **Açıklanabilirlik:** SHAP (Shapley Additive exPlanations)
- **Metriks:** F1-Score, ROC-AUC

## Proje Yönetim Takvimi

| Hafta | Tarih | Yapılacak İşlemler |
|-------|-------|-------------------|
| 1 | 09-15 Mart | EDA, Veri Seti Temini, Literatür Taraması |
| 2 | 16-22 Mart | Veri Ön İşleme (Eksik Veriler, Aykırı Değerler) |
| 3 | 23-29 Mart | Özellik Mühendisliği (Finansal Rasyolar) |
| 4 | 30 Mar-05 Nis | Model Geliştirme (XGBoost, Random Forest) |
| 5 | 06-12 Nisan | XAI Entegrasyonu (SHAP) |
| 6 | 13-19 Nisan | Model Optimizasyonu (GridSearch) |
| 7 | 20-26 Nisan | Backend Altyapısı (FastAPI) |
| 8 | 27 Nis-03 May | Frontend Başlangıç (React.js Setup) |
| 9 | 04-10 Mayıs | Frontend-Backend Entegrasyonu |
| 10 | 11-17 Mayıs | Görselleştirme & Dashboard |
| 11 | 18-24 Mayıs | Test & Hata Ayıklama |
| 12 | 25-31 Mayıs | Dokümantasyon & Sunum |

## Proje Yapısı

```
FINTAG/
├── frontend/               # React.js arayüz
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.tsx
│   └── package.json
├── backend/                # FastAPI servisi
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── routes/
│   ├── requirements.txt
│   └── config.py
├── ml_models/              # Makine Öğrenmesi componentleri
│   ├── training/
│   ├── evaluation/
│   ├── explainability/     # SHAP analizidir
│   └── models/             # Eğitilmiş modeller
├── notebooks/              # Jupyter Notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_xai_analysis.ipynb
├── data/                   # Veri setleri
│   ├── raw/
│   ├── processed/
│   └── external/
├── docs/                   # Dokümantasyon
│   ├── ARCHITECTURE.md
│   ├── API_DOCS.md
│   └── TIMELINE.md
└── README.md
```

## Kaynaklar
- Miuul. (2026). Veri Bilimi ve Makine Öğrenmesi Eğitimi: Kredi Risk Analizi
- McKinney, W. (2012). Python for Data Analysis
- Scikit-learn Developers. (2024). Decision Trees and Random Forests

## İş Sağlığı & Güvenliği
- Çalışma periyotlarında 20 dakikada bir 20 saniye uzağa bakma (20-20-20 kuralı)
