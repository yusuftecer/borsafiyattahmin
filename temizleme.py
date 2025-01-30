import pandas as pd


# BIST 30 hisseleri sembolleri
bist30_symbols = [
    'AKBNK.E', 'ARCLK.E', 'ASELS.E', 'BIMAS.E', 'EREGL.E', 'FROTO.E', 'GARAN.E',
    'KCHOL.E', 'KRDMD.E', 'KOZAA.E', 'KOZAL.E', 'PGSUS.E', 'SAHOL.E', 'SISE.E',
    'TAVHL.E', 'TCELL.E', 'THYAO.E', 'TKFEN.E', 'TTKOM.E', 'TUPRS.E', 'VAKBN.E', 'YKBNK.E'
]
# 0 değerlerini içeren satırları sil


for j in range(16,19):
    for i in range(1, 13):
        a = str(i)
        b= str(j)
        if a != "10" and a != "11" and a != "12":
            isim = "PP_GUNSONUFIYATHACIM.M.20" + b + "0" + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isim
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[20],
                                                                  df.columns[21], df.columns[22], df.columns[24],
                                                                  df.columns[27],df.columns[28], df.columns[29]]]
            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/"+"20"+ b + "0" + a +"BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()
        else:
            isimi = "PP_GUNSONUFIYATHACIM.M.20" + b + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isimi
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[20],
                                                                  df.columns[21], df.columns[22], df.columns[24],
                                                                  df.columns[27],df.columns[28], df.columns[29]]]
            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/" + "20" + b + a + "BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()

for j in range(19,20):
    for i in range(1, 13):
        a = str(i)
        b= str(j)
        if a != "10" and a != "11" and a != "12":
            isim = "PP_GUNSONUFIYATHACIM.M.20" + b + "0" + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isim
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[20],
                                                                  df.columns[21], df.columns[22], df.columns[24],
                                                                  df.columns[27],df.columns[28], df.columns[29]]]
            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/"+"20"+ b + "0" + a +"BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()
        else:
            isimi = "PP_GUNSONUFIYATHACIM.M.20" + b + a + ".csv"

            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isimi
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç


            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[19],
                                                                  df.columns[20], df.columns[21], df.columns[23],
                                                                  df.columns[26],df.columns[27], df.columns[28]]]
            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/" + "20" + b + a + "BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

for j in range(20,25):
    for i in range(1, 13):
        a = str(i)
        b= str(j)
        if a != "10" and a != "11" and a != "12":
            isim = "PP_GUNSONUFIYATHACIM.M.20" + b + "0" + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isim
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[19],
                                                                  df.columns[20], df.columns[21], df.columns[23],
                                                                  df.columns[26],df.columns[27], df.columns[28]]]

            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/"+"20"+ b + "0" + a +"BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()
        else:
            isimi = "PP_GUNSONUFIYATHACIM.M.20" + b + a + ".csv"
            file_path = 'C:/Users/yusuf/Desktop/borsa/veri/' + isimi
            df = pd.read_csv(file_path, sep=';')

            # İlgili sütunları seç

            df_filtered = df[df.iloc[:, 1].isin(bist30_symbols)][[df.columns[0], df.columns[1],
                                                                  df.columns[16], df.columns[17], df.columns[19],
                                                                  df.columns[20], df.columns[21], df.columns[23],
                                                                  df.columns[26],df.columns[27], df.columns[28]]]
            # NaN değerleri sıfır yap
            df_filtered.fillna(0, inplace=True)

            # Verileri sayıya çevir
            df_filtered.iloc[:, 2:] = df_filtered.iloc[:, 2:].astype(float)  # 2. sütundan itibaren tümünü float yap

            # kapanış fiyatı 0 olan satırları sil
            df_filtered = df_filtered[df_filtered['KAPANIS FIYATI'] != 0]

            # Sonuçları kaydet
            son = "C:/Users/yusuf/Desktop/tem veri2/" + "20" + b + a + "BIST30_Kapanis_Fiyatlari.csv"
            df_filtered.to_csv(son, index=False)

            df_filtered.head()




