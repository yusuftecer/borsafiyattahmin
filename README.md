# borsafiyattahmin 
 

Bu proje, **Borsa İstanbul (BIST)** verileri kullanılarak hisse senedi fiyatlarını tahmin etmek için **XGBoost regresyon modeli** ile geliştirilmiştir. Model, **8 yıllık borsa işlem verisi** ile eğitilmiş olup, teknik indikatörler yerine doğrudan **ham piyasa verilerini** kullanmaktadır.  



### 🚀 Özellikler:  

✅ **8 Yıllık Tarihsel Veri**: 2017-2025 arasındaki işlem verileri kullanılarak model eğitilmiştir.  

✅ **XGBoost Algoritması**: Güçlü ve optimize edilmiş gradient boosting tabanlı regresyon modeli.  

✅ **Ham Borsa Verileri**:  

   - Önceki Kapanış Fiyatı

   -    - Açılış Fiyatı
    
        -    - En Düşük & En Yüksek Fiyat
         
             -    - Günlük Yüzdelik Değişim (%)
              
                  -    - Ağırlıklı Ortalama Fiyat (A.O.F)
                   
                       -    - Toplam İşlem Hacmi & Toplam İşlem Adedi
                        
                            - ✅ **Veri Ön İşleme**: Eksik verilerin temizlenmesi ve MinMaxScaler ile normalizasyon.
                        
                            - ✅ **Zaman Serisi Modelleme**: Son **60 günlük fiyat verisi** kullanılarak gelecekteki fiyat tahminleri yapılıyor.
                        
                            - ✅ **Görselleştirme**: Tahmin edilen fiyatlar ile gerçek fiyatlar karşılaştırılarak performans analizi yapılıyor.
                        
                  -    ### 📊 Kullanım Alanları:
              
                  -    🔹 Hisse senedi fiyat tahminleme
              
                  -    🔹 Finansal veri analizi
              
                  -    🔹 Algo-trading & Backtesting
              
        -    Bu proje, yatırımcılar, veri bilimciler ve finansal analizle ilgilenen herkes için güçlü bir tahminleme modeli sunmaktadır. 🚀
