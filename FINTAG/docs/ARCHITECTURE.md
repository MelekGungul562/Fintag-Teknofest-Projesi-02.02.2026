# FINTAG Mimarisi

## Sistem Bileşenleri

### 1. Frontend (React.js + Tailwind CSS)

**Görevler:**
- Kullanıcı arayüzü sağlama
- Kredi başvurusu formu
- Model tahminleri ve açıklamaları görselleştirme
- XAI grafiklerini dashboard'da gösterme

**Teknolojiler:**
- React.js: Bileşen tabanlı mimarisi
- Tailwind CSS: Modern arayüz tasarımı
- Axios: API çağrıları
- Recharts: Veri görselleştirme

### 2. Backend (FastAPI + Python)

**Görevler:**
- REST API endpoints sağlama
- Model tahminleri gerçekleştirme
- XAI açıklamaları hesaplama
- Veri doğrulama ve işleme

**Teknolojiler:**
- FastAPI: Asenkron web framework
- Pydantic: Veri doğrulama
- SQLAlchemy: Veritabanı ORM (opsiyonel)

### 3. Makine Öğrenmesi Modelleri

**Eğitlenmesi Planlanan Algoritmalar:**
1. **XGBoost** (başlıca aday)
2. **Random Forest** (karşılaştırma)
3. **CatBoost** (karşılaştırma)

**Performans Metrikleri:**
- F1-Score
- ROC-AUC
- Precision, Recall
- Cross-validation scores

### 4. Açıklanabilirlik (XAI)

**SHAP (SHapley Additive exPlanations) Kullanımı:**
- Her finansal özniteliğin karar üzerindeki etkisini gösterme
- Shapley Değerleri ile matematiksel açıklanabilirlik
- Interactive SHAP grafikleri

## Veri Akışı

```
Kullanıcı (Frontend)
    ↓
    → Kredi Başvurusu Formu
    ↓
Backend API
    ↓
    → Veri Doğrulama (Pydantic)
    → Veri Ön İşleme
    ↓
Makine Öğrenmesi Pipeline
    ↓
    → Model Tahmin: Kredi Onaylanır mı?
    → SHAP Açıklaması: Neden?
    ↓
Backend Yanıtı
    ↓
Frontend Dashboard
    ↓
    → Tahmin Sonucu (Onay/Red)
    → XAI Grafikler
    → Finansal Rasyolar
```

## Geliştirme Fazları

1. **EDA & Veri Hazırlığı** (Haftalar 1-2)
2. **Özellik Mühendisliği** (Hafta 3)
3. **Model Geliştirme** (Haftalar 4-6)
4. **Backend Kurulumu** (Hafta 7)
5. **Frontend Geliştirmesi** (Haftalar 8-10)
6. **Test & Optimizasyon** (Hafta 11)
7. **Dokümantasyon & Sunumu** (Hafta 12)
