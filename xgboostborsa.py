import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# 1. Veriyi Yükleme
file_path = "C:/Users/yusuf/Desktop/output3/TTKOM.E_combined_data.csv"
data = pd.read_csv(file_path)

# 2. Tarih formatını ayarlama ve sıralama
data['TARIH'] = pd.to_datetime(data['TARIH'])  # Tarih formatı
data = data.sort_values(by='TARIH')  # Tarih sırasına göre sıralama

# 3. Kullanılacak özellikler (indikatörler hariç)
features = ['ONCEKI KAPANIS FIYATI', 'ACILIS FIYATI', 'EN DUSUK FIYAT', 'EN YUKSEK FIYAT',
            'DEGISIM (%)', 'A.O.F', 'TOPLAM ISLEM HACMI', 'TOPLAM ISLEM ADEDI']

# 4. Veriyi Temizleme ve Normalleştirme
data = data.dropna()  # Eksik verileri temizliyoruz

# Özelliklerin normalizasyonu
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data[features])

# 5. Eğitim ve Test Verilerini Ayırma
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]

# 6. Dataset Oluşturma Fonksiyonu (X ve y)
def create_dataset(dataset, time_step=30):
    X, y = [], []
    for i in range(len(dataset) - time_step):
        X.append(dataset[i:i + time_step])
        y.append(dataset[i + time_step, 0])  # Kapanış fiyatını hedef olarak alıyoruz
    return np.array(X), np.array(y)

time_step = 30  # Son 60 günü kullanarak tahmin yap
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# XGBoost için uygun formatta veriyi düzenleme
X_train_reshaped = X_train.reshape(X_train.shape[0], -1)  # Her bir zaman dilimini düzleştiriyoruz
X_test_reshaped = X_test.reshape(X_test.shape[0], -1)

# 7. XGBoost Modeli
model = xgb.XGBRegressor(n_estimators=100, random_state=42, objective='reg:squarederror', eval_metric='rmse')
model.fit(X_train_reshaped, y_train)

# 8. Tahmin
predictions = model.predict(X_test_reshaped)

# 9. Tahmin Sonuçlarını Görselleştirme
real_prices = scaler.inverse_transform(test_data[time_step:])[:, 0]  # Gerçek fiyatlar
predicted_prices = scaler.inverse_transform(np.concatenate((predictions.reshape(-1, 1), np.zeros((predictions.shape[0], len(features)-1))), axis=1))[:, 0]

# Grafik
plt.figure(figsize=(12, 6))
plt.plot(real_prices, label="Gerçek Fiyatlar")
plt.plot(predicted_prices, label="XGBoost Tahminleri", linestyle='--')
plt.legend()
plt.show()
