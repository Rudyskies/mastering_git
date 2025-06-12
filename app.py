import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

st.title("📊 Dashboard Penjualan Toko Online")

# --- Data Produk ---
produk_data = {
    'id_produk': [1, 2, 3, 4, 5],
    'nama_produk': ['Kaos', 'Celana', 'Jaket', 'Topi', 'Hoodie'],
    'harga': [50000, 100000, 150000, 30000, 200000]
}
produk_df = pd.DataFrame(produk_data)

# --- Generate Data Penjualan Dummy ---
@st.cache_data
def generate_penjualan():
    penjualan = []
    id_transaksi = 1
    tanggal_awal = datetime(2025, 6, 1)
    for hari in range(30):
        tanggal = tanggal_awal + timedelta(days=hari)
        for _ in range(random.randint(2, 6)):
            id_produk = random.choice(produk_data['id_produk'])
            jumlah = random.randint(1, 5)
            penjualan.append([id_transaksi, id_produk, jumlah, tanggal.date()])
            id_transaksi += 1
    return pd.DataFrame(penjualan, columns=['id_transaksi', 'id_produk', 'jumlah', 'tanggal'])

penjualan_df = generate_penjualan()

# --- Gabungkan Data ---
gabung_df = penjualan_df.merge(produk_df, on='id_produk')
gabung_df['total_uang'] = gabung_df['jumlah'] * gabung_df['harga']

# --- Tampilkan Tabel ---
st.subheader("📋 Tabel Penjualan")
st.dataframe(gabung_df)

# --- Analisis ---
total_terjual = gabung_df.groupby('nama_produk')['jumlah'].sum().sort_values(ascending=False)
total_omzet = gabung_df.groupby('nama_produk')['total_uang'].sum().sort_values(ascending=False)
penjualan_harian = gabung_df.groupby('tanggal')['total_uang'].sum()

# --- Visualisasi ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Total Item Terjual per Produk")
    fig1, ax1 = plt.subplots()
    total_terjual.plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_ylabel("Jumlah")
    ax1.set_xlabel("Produk")
    ax1.set_title("Total Item Terjual")
    ax1.grid(axis='y')
    st.pyplot(fig1)

with col2:
    st.subheader("💰 Omzet per Produk (Pie Chart)")
    fig2, ax2 = plt.subplots()
    total_omzet.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax2)
    ax2.set_ylabel("")
    ax2.set_title("Omzet per Produk")
    st.pyplot(fig2)

st.subheader("📈 Tren Omzet Harian")
fig3, ax3 = plt.subplots()
penjualan_harian.plot(marker='o', linestyle='-', ax=ax3)
ax3.set_ylabel("Total Uang")
ax3.set_xlabel("Tanggal")
ax3.tick_params(axis='x', rotation=90)
ax3.set_title("Tren Penjualan Harian")
ax3.grid(True)
st.pyplot(fig3)