import os
import glob
import pandas as pd

# Dosya yolu ve dosya adları
folder_path = 'C:/Users/yusuf/Desktop/tem veri2'  # CSV dosyalarının bulunduğu klasör yolu
all_files = glob.glob(os.path.join(folder_path, '*.csv'))  # Tüm CSV dosyalarını al

# Tüm CSV dosyalarını okuyup tek bir DataFrame'e birleştir
df_list = []
for file in all_files:
    df = pd.read_csv(file, delimiter=',', header=0)  # header=0 ile dosyanın ilk satırı sütun adları olarak kullanılır
    df_list.append(df)

# Tüm DataFrame'leri birleştir
combined_df = pd.concat(df_list, ignore_index=True)

# Tarih sütununu datetime formatına dönüştür
combined_df['TARIH'] = pd.to_datetime(combined_df['TARIH'])

# Hisse ismine göre gruplayın ve işlemleriniz için devam edin
grouped_df = combined_df.groupby('ISLEM  KODU')

# Gruplandıktan sonra örnek olarak ilk hisse için veriyi göstermek için
print(grouped_df.get_group('THYAO.E'))

# Sonuçları başka bir CSV dosyasına yazdırabilirsiniz

output_folder = 'C:/Users/yusuf/Desktop/output3/'  # Çıktı dosyalarının klasörü
os.makedirs(output_folder, exist_ok=True)  # Klasörü oluştur (varsa geçersiz kıl)

for sembol, data in grouped_df:
    output_file = os.path.join(output_folder, f'{sembol}_combined_data.csv')
    data.to_csv(output_file, index=False)  # Index sütununu yazma

output_file = 'C:/Users/yusuf/Desktop/combined_data.csv'  # Çıktı dosyasının yolu ve adı
grouped_df.to_csv(output_file)