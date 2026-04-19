# FINTAG Proje Takvimi

## Haftalık Kilometre Taşları

### Hafta 1: 09-15 Mart
**Hedefler:**
- [ ] Veri seti (LoanDB) temin edilmesi
- [ ] Keşifçi veri analizi (EDA) yapılması
- [ ] Literatür taraması tamamlanması
- [ ] Proje dokumentasyonu başlatılması

**Çıktılar:**
- `notebooks/01_EDA.ipynb` - Veri keşfi raporlaması
- Veri seti wrangling notları

---

### Hafta 2: 16-22 Mart
**Hedefler:**
- [ ] Eksik verilerin tamamlanması (Pandas)
- [ ] Aykırı değer (outlier) analizi
- [ ] Veri temizliği adımları
- [ ] Veri kalitesi raporu

**Çıktılar:**
- `notebooks/02_preprocessing.ipynb` - Ön işleme adımları
- Temiz veri seti

---

### Hafta 3: 23-29 Mart
**Hedefler:**
- [ ] Finansal rasyoların (özellik) üretilmesi
- [ ] Özellik seçimi (feature selection)
- [ ] Bağımsız değişkenler arasında korelasyon analizi
- [ ] Model başarısını artıracak özellikler belirlenmesi

**Çıktılar:**
- `notebooks/03_feature_engineering.ipynb` - Özellik mühendisliği
- Feature matrix hazırlanması

---

### Hafta 4: 30 Mart - 05 Nisan
**Hedefler:**
- [ ] Model eğitim seti ve test seti ayrılması
- [ ] XGBoost algoritmasının eğitilmesi
- [ ] Random Forest algoritmasının eğitilmesi
- [ ] Parametre ayarı (hyperparameter tuning) başlangıcı

**Çıktılar:**
- `notebooks/04_model_training.ipynb` - Model eğitimi
- Ilk model karşılaştırması

---

### Hafta 5: 06-12 Nisan
**Hedefler:**
- [ ] SHAP kütüphanesinin entegrasyonu
- [ ] Model kararlarının açıklanması
- [ ] SHAP görselleştirmeleri (SHAP values, force plots)
- [ ] XAI raporunun hazırlanması

**Çıktılar:**
- `notebooks/05_xai_analysis.ipynb` - Açıklanabilirlik analizi
- SHAP visualization örnekleri

---

### Hafta 6: 13-19 Nisan
**Hedefler:**
- [ ] GridSearch ile hiperparametre optimizasyonu
- [ ] En iyi modelin seçilmesi (F1-Score, ROC-AUC kriterlerine göre)
- [ ] Cross-validation sonuçları
- [ ] Final model eğitimi

**Çıktılar:**
- Optimized model (`ml_models/models/best_model.pkl`)
- Hiperparametre raporlaması

---

### Hafta 7: 20-26 Nisan
**Hedefler:**
- [ ] FastAPI backend yapısı kurulması
- [ ] Model yükleme ve tahmin endpoints'leri
- [ ] SHAP açıklaması endpoint'i
- [ ] API dokümantasyonu (Swagger UI)

**Çıktılar:**
- `backend/main.py` - FastAPI uygulaması
- `/predict` ve `/explain` endpoints
- Swagger API dokümanları

---

### Hafta 8: 27 Nisan - 03 Mayıs
**Hedefler:**
- [ ] React.js projesinin kurulması
- [ ] Tailwind CSS konfigürasyonu
- [ ] Temel bileşenler (components) geliştirilmesi
- [ ] Arayüz iskeletinin oluşturması

**Çıktılar:**
- React proje yapısı
- Kredi başvurusu formu bileşeni

---

### Hafta 9: 04-10 Mayıs
**Hedefler:**
- [ ] React ile FastAPI API çağrıları (Axios/Fetch)
- [ ] Veri akışının test edilmesi (end-to-end)
- [ ] Form validation ve error handling
- [ ] Loading states ve user feedback

**Çıktılar:**
- Fonksiyonel frontend-backend bağlantısı
- API call testleri

---

### Hafta 10: 11-17 Mayıs
**Hedefler:**
- [ ] Tahmin sonuçlarının görselleştirilmesi
- [ ] SHAP grafiklerinin dashboard'a eklenmesi
- [ ] Finansal rasyoların gösterilmesi
- [ ] İnteraktif dashboard elemanları

**Çıktılar:**
- Kredi sonuç dashboard'ı
- XAI görselleştirmeleri (SHAP, önem grafikleri)

---

### Hafta 11: 18-24 Mayıs
**Hedefler:**
- [ ] End-to-end fonksiyonel testler
- [ ] Hata ayıklama (debugging)
- [ ] Model doğrulaması (validation)
- [ ] Performance testi

**Çıktılar:**
- Test raporu
- Hata ve çözüm dokümantasyonu

---

### Hafta 12: 25-31 Mayıs
**Hedefler:**
- [ ] Teknik rapor yazılması
- [ ] Kullanıcı dokümantasyonu
- [ ] Sunum hazırlığı
- [ ] Demo hazırlanması

**Çıktılar:**
- Teknik Rapor (PDF)
- Kullanım Kılavuzu
- Sunum Yeterliği

---

## Maliyet Tahminlemesi

| Kategori | Bütçe |
|----------|-------|
| Domain Alan Adı | 500 TL |
| Veri Seti | 0 TL (Açık kaynak) |
| Geliştirme Araçları | 0 TL (Free versions) |
| **Toplam** | **500 TL** |

## İş Sağlığı & Güvenliği

- **20-20-20 Kuralı:** Her 20 dakikada bir, 20 saniye boyunca 20 feet (6 meter) uzağa bakma
