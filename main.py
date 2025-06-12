import pandas as pd
import numpy as np
import re

# Data contoh
data = {
    'No': [1,2,3,4,5,6,7],
    'Nama': ['Budi', 'Ani', 'Joko', None, 'Dewi', 'Rina', 'Dedi'],
    'Tanggal Lahir': ['12/05/1990', 'NULL', '1993-08-17', '10/10/1985', '1980/01/01', '31-12-1989', '1990.07.15'],
    'Gaji': ['5.000.000', '6.000.000', '5jt', '-', '7.000.000', 'unknown', '0'],
    'Aktif': ['ya', 'Ya', 'Y', 'tidak', 'tdk', 'aktif', 'no']
}

df = pd.DataFrame(data)

# --- Bersihkan tanggal lahir ---
def parse_dates(x):
    try:
        # Coba parse dengan dayfirst=True
        return pd.to_datetime(x, dayfirst=True, errors='coerce')
    except:
        return pd.NaT

df['Tanggal Lahir'] = df['Tanggal Lahir'].apply(parse_dates)

# --- Bersihkan kolom Gaji ---
def clean_gaji(gaji):
    if isinstance(gaji, str):
        gaji = gaji.lower()
        # Tangani nilai-nilai tak valid
        if gaji in ['-', 'unknown', 'null', '0', 'don\'t know', 'blank', 'error']:
            return np.nan
        # Tangani format 5jt jadi 5000000
        if 'jt' in gaji:
            angka = re.findall(r'\d+', gaji)
            if angka:
                return int(angka[0]) * 1_000_000
            else:
                return np.nan
        # Hapus tanda titik dan coba konversi
        gaji = gaji.replace('.', '')
        try:
            return int(gaji)
        except:
            return np.nan
    elif isinstance(gaji, (int, float)):
        return gaji
    else:
        return np.nan

df['Gaji'] = df['Gaji'].apply(clean_gaji)

# --- Standarkan kolom Aktif ---
def clean_aktif(val):
    if isinstance(val, str):
        val = val.lower()
        if val in ['ya', 'y', 'aktif', 'yes', 'true', '1']:
            return True
        elif val in ['tidak', 'tdk', 'no', 'false', '0']:
            return False
    return False

df['Aktif'] = df['Aktif'].apply(clean_aktif)

print(df)